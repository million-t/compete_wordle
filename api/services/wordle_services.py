from api.models import Word
from api.utils.wordle_logic import evaluate_guess

def process_word_guess(guess_text, word_id):
    target_word = Word.objects.get(pk=int(word_id)).word_text
    response = evaluate_guess(guess_text, target_word)
    return response