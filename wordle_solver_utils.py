import re

def remove_words_with_forbidden_characters(words, list_of_forbidden_chars): 
    return_list = []


    for word in words:
        skip = False
        for char in list_of_forbidden_chars:
            if char in word:
                skip = True
        
        if not skip:
            return_list.append(word) 

    return return_list

def keep_words_with_necessary_characters(words, list_of_necessary_chars): 
    return_list = []

    for word in words:
        all_chars_found = True
        for char in list_of_necessary_chars:
            
            if char not in word:
                
                all_chars_found = False

        if all_chars_found:
            return_list.append(word)

    return return_list

def remove_words_that_match_pattern(words, pattern):
    return_list = []

    matcher = re.compile(pattern)
    for word in words:
        
        
        if not matcher.match(word):
            return_list.append(word) 

    return return_list

def keep_words_that_match_pattern(words, pattern):
    return_list = []

    matcher = re.compile(pattern)
    for word in words:
        
        
        if matcher.match(word):
            return_list.append(word) 

    return return_list


def score_words(words, scoring_dict):

    scores = []
    for word in words:        
        word_score = 0
        for char in word:
            char_score = scoring_dict[char]
            if word.count(char) > 1:
                char_score /= 4

            word_score += char_score

        scores.append(word_score)

    return scores


def eliminate_words_based_on_guess(guess, result_of_guess, words):
    list_of_forbidden_chars = []
    list_of_necessary_chars = []
    patterns_to_eliminate = []
    patterns_to_keep = []


    result_of_guess = result_of_guess.upper()

    for i in range(5):
        guess_char = guess[i]
        result_char = result_of_guess[i]

        if result_char == 'X':
            list_of_forbidden_chars.append(guess_char)
        elif result_char == 'Y':
            list_of_necessary_chars.append(guess_char)

            pattern = '.'*(i) + guess_char + '.' * (4-i)
            patterns_to_eliminate.append(pattern)

        elif result_char == 'G':
            list_of_necessary_chars.append(guess_char)

            pattern = '.'*(i) + guess_char + '.' * (4-i)
            patterns_to_keep.append(pattern)

    words = remove_words_with_forbidden_characters(words, list_of_forbidden_chars)
    words = keep_words_with_necessary_characters(words, list_of_necessary_chars)

    for pattern in patterns_to_eliminate:
        words = remove_words_that_match_pattern(words, pattern)
    for pattern in patterns_to_keep:
        words = keep_words_that_match_pattern(words, pattern) 

    return words

def make_letter_dict(words):
    letter_dict = {}

    for word in words:
        for char in word:
            
            if char not in letter_dict.keys():
                letter_dict[char] = 1
            else:
                letter_dict[char] += 1

    return letter_dict


def find_options(words, n_options):

    letter_dict = make_letter_dict(words)

    scores = score_words(words, letter_dict)

    sorted_options = [x for _, x in sorted(zip(scores, words), reverse=True)]

    return sorted_options[:n_options]

