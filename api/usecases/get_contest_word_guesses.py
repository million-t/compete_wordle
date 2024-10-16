from api.repositories.guess_repository import get_word_guesses
from api.serializers import GuessSerializer
from api.utils.wordle_logic import evaluate_guess
from api.repositories.word_repository import get_word_by_id

def get_contest_word_guesses_usecase(contest_id, user_id, word_id):
    guesses = get_word_guesses(contest_id, user_id, word_id)
    word = get_word_by_id(word_id)

    # print(guesses)
    # guesses = GuessSerializer(guesses, many=True).data
    # print(guesses)
    if not word:
        raise ValueError("Word doesn't exist.")
    res = []
    for i in range(len(guesses)):
        guess = GuessSerializer(guesses[i]).data
        score =  evaluate_guess(guess['guess_text'], word.word_text)
        res.append({
            'id': guess['id'],
            'guess_text': guess['guess_text'],
            'timestamp': guess['timestamp'],
            'score': score
        })
        # res.append(evaluate_guess(guesses[i]['guess_text'], guesses[i]['word_text']))


    return res