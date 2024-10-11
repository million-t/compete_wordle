from api.repositories.contest_participant_repository import get_contest_participants_by_contest
from django.core.paginator import Paginator

def get_standings_usecase(contest_id, page, page_size):
    participants = get_contest_participants_by_contest(contest_id)
    paginator = Paginator(participants, page_size)
    paginated_participants = paginator.get_page(page)
    off_set = paginated_participants.start_index()
    standings = [
        {
            'user': participant.user.username,
            'score': participant.score,
            'rank': off_set + index
        }
        for index, participant in enumerate(paginated_participants)
    ]


    return {
        'standings': standings,
        'page': paginated_participants.number,
        'page_size': page_size,
        'total_pages': paginator.num_pages,
        'total_participants': paginator.count
    }