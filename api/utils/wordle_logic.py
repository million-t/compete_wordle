from collections import defaultdict

def evaluate_guess(guess_text, target_word):
    guess_list = list(guess_text)
    target_list = list(target_word)
    
    word_len = len(target_word)
    result = [1]*word_len
    perfect_count = 0

    for i in range(word_len):
        if guess_list[i] == target_list[i]:
            target_list[i] = "#"
            guess_list[i] = "$"
            perfect_count += 1
            result[i] = 3

    correct = perfect_count == word_len
    count = defaultdict(int)
    for char in target_list:
        if char != '#':
            count[char] += 1
    
    for i, char in enumerate(guess_list):
        if guess_list[i] != '$' and count[char]:
            count[char] -= 1
            result[i] = 2

    response = {
        "message": "Guess evaluated.",
        "data": result,
        "correct": correct,
    }

    return response
