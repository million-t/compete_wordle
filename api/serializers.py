from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Word, Contest, Guess, ContestParticipant, InvitationCode


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = ['id', 'title', 'start_time', 'end_time', 'participants', 'contest_type', 'contest_availability', 'description', 'created_at']

class InvitationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationCode
        fields = '__all__'

class GuessSerializer(serializers.ModelSerializer):
    guess_text = serializers.CharField(max_length=5)
    class Meta:
        model = Guess
        fields = '__all__'

class ContestParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestParticipant
        fields = '__all__'

