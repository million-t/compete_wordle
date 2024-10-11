from api.repositories.word_repository import get_word_by_id
from api.utils.wordle_logic import evaluate_guess

def process_word_guess_usecase(guess_text, word_id):
    
    target_word = get_word_by_id(word_id)
    if target_word is None:
        raise ValueError("Word doesn't exist.")

    response = evaluate_guess(guess_text, target_word.word_text)
    return response