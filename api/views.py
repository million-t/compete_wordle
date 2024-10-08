from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Word, Contest, Guess, ContestParticipant
from .serializers import WordSerializer, ContestSerializer, GuessSerializer, ContestParticipantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from collections import defaultdict

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
            
            target_word = Word.objects.get(pk=int(word)).word_text
            
            guess_list = list(guess_text)
            target_list = list(target_word)
            
            word_len = len(target_word)
            res = [0]*word_len
            perfect_count = 0

            for i in range(word_len):
                if guess_list[i] == target_list[i]:
                    guess_list[i] = "$"
                    target_list[i] = "#"
                    res[i] = 2
                    perfect_count += 1

            if perfect_count == word_len:
                
                # complete word guess logic


                return Response({'message':'Correctly guessed!', 'data': res}, status=status.HTTP_200_OK)

            count = defaultdict(int)
            for char in target_list:
                if char != '#':
                    count[char] += 1
            
            for i, char in enumerate(guess_list):
                if guess_list[i] != '$' and count[char]:
                    count[char] -= 1
                    res[i] = 1
            
            
            return Response({'message':'Guess evaluated.', 'data': res}, status=status.HTTP_200_OK)
            
        except:
            return Response({'error': 'Word does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({"guess_text":guess_text}, status=status.HTTP_200_OK)

        # if len(guess_word) != 5:
        #     return Response({'error': 'Guess must be a 5-letter word'}, status=status.HTTP_400_BAD_REQUEST)
        
        # is_correct = guess_word == round_instance.word_to_guess.lower()

        # guess = Guess.objects.create(
        #     user_id = request.user,
            
        # )

        # if is_correct:
        #     return Response({'message': 'Correct guess!', 'data': GuessSerializer(guess).data}, status=status.HTTP_200_OK)
        # else:
        #     return Response({'message': 'Incorrect guess', 'data': GuessSerializer(guess).data}, status=status.HTTP_200_OK)


class GuessViewSet(viewsets.ModelViewSet):
    queryset = Guess.objects.all()
    serializer_class = GuessSerializer

class ContestParticipantViewSet(viewsets.ModelViewSet):
    queryset = ContestParticipant.objects.all()
    serializer_class = ContestParticipantSerializer

