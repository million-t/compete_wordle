from api.repositories.word_repository import get_words_by_contest_id
from api.serializers import WordSerializer

def get_words_usecase(contest_id):
    words = get_words_by_contest_id(contest_id)
    
    if words is None:
        raise ValueError("Encountered an error getting words.")
    
    words = WordSerializer(words, many=True).data
    return words