from api.repositories.contest_repository import get_my_contests
from api.repositories.user_repository import get_user_by_username
from api.serializers import ContestSerializer

def get_my_contests_usecase(username):
    user = get_user_by_username(username)
    if user is None:
        raise ValueError("User not found.")
    my_contests = get_my_contests(user.id)
    my_contests = ContestSerializer(my_contests, many=True).data
    return my_contests

