from api.models import Word

def get_word_by_id(word_id):
    try:
        return Word.objects.get(pk=int(word_id))
    except Word.DoesNotExist:
        return None

def get_word_weight_by_id(word_id):
    try:
        return Word.objects.get(pk=int(word_id)).weight
    except Word.DoesNotExist:
        return None

def get_words_by_contest_id(contest_id):
    try:
        return Word.objects.filter(contest=contest_id)
    
    except Word.DoesNotExist:
        return None

def bulk_create(word_objects):
    try:
        return Word.objects.bulk_create(word_objects)
    except:
        return None
        