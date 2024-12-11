import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Contest(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT, related_name='created_contests')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    participants = models.ManyToManyField(User, through="ContestParticipant", related_name='participated_contests')
    contest_type = models.CharField(
        max_length=10,
        choices=[
            ('DAILY', 'Daily'),
            ('CONTEST', 'Contest')
        ],
        default='CONTEST'
    )
    contest_availability = models.CharField(
        max_length=10,
        choices=[
            ('PRIVATE', 'Private'),
            ('PUBLIC', 'Public')
        ],
        default='PUBLIC'
    )
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        indexes = [
            models.Index(fields=['start_time', 'end_time']),
        ]

    def __str__(self):
        return self.title

class InvitationCode(models.Model):
    contest = models.OneToOneField(Contest, on_delete=models.CASCADE)
    code = models.CharField(max_length=36, unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.code

class Word(models.Model):
    word_text = models.CharField(max_length=5)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    word_position = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField(default=1)

    def __str__(self):
        return f"Target word: {self.word_text}"

class Guess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word_position = models.CharField(max_length=2)
    guess_text = models.CharField(max_length=5)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s guess: {self.guess_text}"


class ContestParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} in {self.contest.title} with score: {self.score}"


class Leaderboard(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    trials = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    rank = models.IntegerField()

    class Meta:
        unique_together = ('contest', 'user', 'word')
        indexes = [
            models.Index(fields=['contest', 'word', '-score']),
        ]

    def __str__(self):
        return f"{self.user.username} in {self.contest.title} for word {self.word.word_text} with score: {self.score} and rank: {self.rank}"
