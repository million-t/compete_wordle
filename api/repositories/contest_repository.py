from api.models import Contest

def get_contest_by_id(contest_id):
    try:
        return Contest.objects.get(pk=contest_id)
    except Contest.DoesNotExist:
        return None

def create_contest(validated_data):
    return Contest.objects.create(**validated_data)

def get_my_contests(user):
    res = Contest.objects.filter(creator=user)
    return res