from django.db import transaction
from api.models import Guess

def get_word_guesses(contest_id, user_id, word_id):
    guesses = Guess.objects.filter(contest=contest_id, user=user_id, word=word_id)
    return guesses


def submit_new_guess(contest_id, user_id, word_id, guess_text):
    with transaction.atomic():
        new_guess = Guess(contest_id=contest_id, user_id=user_id, word_id=word_id, guess_text=guess_text)
        new_guess.save()
    return new_guess