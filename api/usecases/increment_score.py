from django.db import transaction
from api.repositories.word_repository import get_word_weight_by_id
from api.repositories.contest_participant_repository import get_contest_participant_by_user

def increment_score_usecase(participant, word_id):
    
    word_weight = get_word_weight_by_id(word_id)
    if word_weight is None:
        raise ValueError("Word doesn't exist.")

    contest_participant = get_contest_participant_by_user(participant)
    if contest_participant is None:
        raise ValueError("Invalid participant.")
    
    with transaction.atomic():
        contest_participant.score += word_weight
        contest_participant.save()

    return contest_participant.score

