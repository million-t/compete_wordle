from django.db import transaction
from api.repositories.contest_repository import get_contest_by_id
from api.repositories.contest_participant_repository import get_or_create_contest_participant

def register_participant_usecase(contest_id, user):
    contest = get_contest_by_id(contest_id)

    if not contest:
        raise ValueError("Invalid contest ID.")
    
    with transaction.atomic():
        participant, created = get_or_create_contest_participant(contest, user)
    return participant