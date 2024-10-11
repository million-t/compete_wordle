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

