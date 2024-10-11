from api.usecases.process_word_guess import process_word_guess_usecase
from api.usecases.increment_score import increment_score_usecase

def process_word_guess(guess_text, word_id):
    return process_word_guess_usecase(guess_text, word_id)

def increment_score(participant, word_id):
    return increment_score_usecase(participant, word_id)