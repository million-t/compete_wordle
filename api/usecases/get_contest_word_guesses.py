from api.repositories.guess_repository import get_word_guesses
from api.serializers import GuessSerializer
from api.utils.wordle_logic import evaluate_guess

def get_contest_word_guesses_usecase(contest_id, user_id, word_id):
    guesses = get_word_guesses(contest_id, user_id, word_id)
    guesses = GuessSerializer(guesses, many=True).data
    
    # res = []
    # for i in range(len(guesses)):
    #     res.append(evaluate_guess(guesses[i]['guess_text'], guesses[i]['word_text']))

    return guesses