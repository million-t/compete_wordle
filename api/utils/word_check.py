import json
import os

def load_words(file_path=None):
    if file_path is None:
        file_path = os.path.join(os.path.dirname(__file__), 'all-words.json')
    with open(file_path, 'r') as file:
        words_list = json.load(file)
    return set(words_list)


VALID_WORDS_SET = load_words()

def is_valid_word(word):
    print(word)
    return word in VALID_WORDS_SET

