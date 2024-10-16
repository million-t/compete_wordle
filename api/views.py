from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Word, Contest, Guess, ContestParticipant
from .serializers import WordSerializer, ContestSerializer, GuessSerializer, ContestParticipantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from collections import defaultdict
from api.services.wordle_services import process_word_guess, increment_score, register_participant, get_standings, get_words, get_my_contests, get_contest_word_guesses

# Create your views here.
class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all().prefetch_related('participants')
    serializer_class = ContestSerializer
    permission_classes = [ IsAuthenticated ]

    def create(self, request, *args, **kwargs):

        data = request.data
        data['creator'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'], url_path='my')
    def get_my(self, request):
        try:
            user = request.user
            contests = get_my_contests(user)
            return Response(contests, status=status.HTTP_200_OK)
        except:
            return Response({'error': "Couldn't get contests"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='get_word_guesses')
    def get_word_guesses(self, request, pk=None):
        try:
            user = request.user
            word_id = request.query_params.get('word_id', None)
            if word_id is None:
                return Response({'error': 'word_id query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            guesses = get_contest_word_guesses(pk, user.id, word_id)
            return Response(guesses, status=status.HTTP_200_OK)
        except:
            return Response({'error': "Couldn't get word guesses"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        try:
            participant = register_participant(pk, request.user)
            return Response({"status": "You have successfuly joined the contest!"}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'], url_path='submit_guess')
    def submit_guess(self, request, pk=None):
        try:
            contest_instance = Contest.objects.get(pk=pk)
        except Contest.DoesNotExist:
            return Response({'error': 'Contest does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        # curr_time = timezone.now()
        # if contest_instance.start_time > curr_time or contest_instance.end_time < curr_time:
        #     return Response({'error': 'Contest is not active'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            guess_text = request.data.get('guess_text', '').lower()
            word_position = request.data.get('word_position', '').upper()
            word = request.data.get('word_id', '')
            user = request.user
            contest = pk
            
        except:
            return Response({'error': 'No enough data provided in the request.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if len(guess_text) != 5:
            return Response({'error': 'Guess must be a 5-letter word'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = process_word_guess(guess_text, word)
        except Word.DoesNotExist:
            return Response({'error': 'Word does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            if response["correct"]:
                score_recorded = increment_score(user, word)
            return Response(response, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Couldn't update score."}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'], url_path='standings')
    def standings(self, request, pk=None):
        try:
            page_number = request.query_params.get('page', 1)
            page_size = request.query_params.get('page_size', 50)
            standings = get_standings(pk, page_number, page_size)
            return Response(standings, status=status.HTTP_200_OK)
        except:
            return Response({'error': "Couldn't get standings"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='words')    
    def get_words(self, request, pk=None):
        try:
            words = get_words(pk)
        except:
            return Response({'error': "Couldn't get words"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(words, status=status.HTTP_200_OK)

class GuessViewSet(viewsets.ModelViewSet):
    queryset = Guess.objects.all()
    serializer_class = GuessSerializer

class ContestParticipantViewSet(viewsets.ModelViewSet):
    queryset = ContestParticipant.objects.all()
    serializer_class = ContestParticipantSerializer

