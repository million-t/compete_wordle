from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Word, Contest, Guess, ContestParticipant
from .serializers import WordSerializer, ContestSerializer, GuessSerializer, ContestParticipantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from collections import defaultdict
from api.services.wordle_services import process_word_guess, increment_score


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

    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        contest = self.get_object()
        user = request.user
        contest.participants.add(user)
        return Response({"status": "You have successfuly joined the contest!"})

    
    
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
                score_recorded = increment_score(participant, word)
                return Response(response, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Couldn't update score."}, status=status.HTTP_400_BAD_REQUEST)
        



class GuessViewSet(viewsets.ModelViewSet):
    queryset = Guess.objects.all()
    serializer_class = GuessSerializer

class ContestParticipantViewSet(viewsets.ModelViewSet):
    queryset = ContestParticipant.objects.all()
    serializer_class = ContestParticipantSerializer

