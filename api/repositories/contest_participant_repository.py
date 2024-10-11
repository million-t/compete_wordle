from api.models import ContestParticipant

def get_contest_participant_by_user(user):
    try:
        return ContestParticipant.objects.get(user=user)
    except ContestParticipant.DoesNotExist:
        return None
        