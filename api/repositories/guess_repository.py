from api.models import Guess

def get_word_guesses(contest_id, user_id, word_id):
    guesses = Guess.objects.filter(contest=contest_id, user=user_id, word=word_id)
    return guesses