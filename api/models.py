from django.db import models
from django.contrib.auth.models import User

class Contest(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT, related_name='created_contests')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    participants = models.ManyToManyField(User, through="ContestParticipant", related_name='participated_contests')

    class Meta:
        indexes = [
            models.Index(fields=['start_time', 'end_time']),
        ]

    def __str__(self):
        return self.title


class Word(models.Model):
    word_text = models.CharField(max_length=5)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    word_position = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)

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