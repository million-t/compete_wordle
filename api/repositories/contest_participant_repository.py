from api.models import ContestParticipant

def get_contest_participant_by_user(user):
    try:
        return ContestParticipant.objects.get(user=user)
    except ContestParticipant.DoesNotExist:
        return None

def get_contest_participants_by_contest(contest):
    return ContestParticipant.objects.filter(contest=contest).select_related('user').order_by('-score')

def get_or_create_contest_participant(contest, user):
    participant, created = ContestParticipant.objects.get_or_create(contest=contest, user=user)
    return participant, created
    