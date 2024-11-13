from api.usecases.process_word_guess import process_word_guess_usecase
from api.usecases.increment_score import increment_score_usecase
from api.usecases.register_participant import register_participant_usecase
from api.usecases.get_standings import get_standings_usecase
from api.usecases.get_words import get_words_usecase
from api.usecases.get_my_contests import get_my_contests_usecase
from api.usecases.get_contest_word_guesses import get_contest_word_guesses_usecase
from api.usecases.create_words import bulk_create_usecase

def process_word_guess(guess_text, word_id, contest_id, user_id):
    return process_word_guess_usecase(guess_text, word_id, contest_id, user_id)

def increment_score(participant, word_id):
    return increment_score_usecase(participant, word_id)

def register_participant(contest_id, user):
    return register_participant_usecase(contest_id, user)

def get_standings(contest_id, page, page_size):
    return get_standings_usecase(contest_id, page, page_size)

def get_words(contest_id):
    return get_words_usecase(contest_id)

def get_my_contests(user):
    return get_my_contests_usecase(user)

def get_contest_word_guesses(contest_id, user_id, word_id):
    return get_contest_word_guesses_usecase(contest_id, user_id, word_id)

def create_words(words):
    return bulk_create_usecase(words)
