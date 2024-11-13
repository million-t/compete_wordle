from api.repositories.contest_participant_repository import get_contest_participants_by_contest
from api.repositories.guess_repository import get_word_guesses
from api.repositories.word_repository import get_words_by_contest_id
from django.core.paginator import Paginator

def get_standings_usecase(contest_id, page, page_size):
    participants = get_contest_participants_by_contest(contest_id)
    paginator = Paginator(participants, page_size)
    paginated_participants = paginator.get_page(page)
    off_set = paginated_participants.start_index()
    words = get_words_by_contest_id(contest_id)

    standings = [

    ]

    pr = [word.id for word in words]
    # print('Words:', pr)
    for participant in paginated_participants:
        row = {
            'user': participant.user.username,
            'score': participant.score,
            'rank': off_set,
            'guesses': [6]*len(words)
        }
        for i, word in enumerate(words):
            guesses = get_word_guesses(contest_id, participant.user.id, word.id)
            # print('Guesses:', participant.user.id, word.id, [guess.guess_text for guess in guesses])
            if not guesses:
                row['guesses'][i] = -1
            for guess in guesses:
                row['guesses'][i] -= guess.guess_text != word.word_text
        standings.append(row)
        
    return {
        'standings': standings,
        'page': paginated_participants.number,
        'page_size': page_size,
        'total_pages': paginator.num_pages,
        'total_participants': paginator.count
    }