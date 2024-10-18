from api.repositories.word_repository import get_word_by_id
from api.repositories.guess_repository import submit_new_guess
from api.utils.wordle_logic import evaluate_guess
from api.repositories.guess_repository import get_word_guesses


def process_word_guess_usecase(guess_text, word_id, contest_id, user_id):
    
    target_word = get_word_by_id(word_id)
    if target_word is None:
        raise ValueError("Word doesn't exist.")

    guess_arr = get_word_guesses(contest_id, user_id, word_id)    
    if len(guess_arr) == 6:
        raise ValueError("Submitted six guesses already.")

    response = evaluate_guess(guess_text, target_word.word_text)
    guess_created = submit_new_guess(contest_id, user_id, word_id, guess_text)
    if not guess_created:
        raise ValueError("Failed to submit guess.")
    return response