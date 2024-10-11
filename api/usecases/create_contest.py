from api.repositories.contest_repository import create_contest
from api.serializers import ContestSerializer

def create_contest_usecase(data, user):
    data['creator'] = user.id
    serializer = ContestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    contest = create_contest(serializer.validated_data)
    return serializer.data, contest

