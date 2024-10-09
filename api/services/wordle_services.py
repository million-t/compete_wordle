from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from api.models import Word, ContestParticipant
from api.utils.wordle_logic import evaluate_guess

def process_word_guess(guess_text, word_id):
    try:
        target_word = Word.objects.get(pk=int(word_id)).word_text
    except ObjectDoesNotExist:
        raise ValueError("word doesn't exist.")

    response = evaluate_guess(guess_text, target_word)
    return response

def increment_score(participant, word_id):
    try:
        word_weight = Word.objects.get(pk=int(word_id)).weight
    except ObjectDoesNotExist:
        raise ValueError("word doesn't exist.")

    try:
        contest_participant = ContestParticipant.objects.get(user=participant)
    
    except ObjectDoesNotExist:
        raise ValueError("Invalid participant.")
    
    with transaction.atomic():
        contest_participant.score += word_weight
        contest_participant.save()

    return contest_participant.score