from api.usecases.process_word_guess import process_word_guess_usecase
from api.usecases.increment_score import increment_score_usecase
from api.usecases.register_participant import register_participant_usecase
from api.usecases.get_standings import get_standings_usecase

def process_word_guess(guess_text, word_id):
    return process_word_guess_usecase(guess_text, word_id)

def increment_score(participant, word_id):
    return increment_score_usecase(participant, word_id)

def register_participant(contest_id, user):
    return register_participant_usecase(contest_id, user)

def get_standings(contest_id, page, page_size):
    return get_standings_usecase(contest_id, page, page_size)