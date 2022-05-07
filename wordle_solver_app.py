import os
import pandas as pd
import numpy as np
import re
import wordle_solver_utils as wordle_utils

filename = './wordle-list-main/words'

with open(filename) as file:
    words = file.readlines()
    words = [line.rstrip() for line in words]

letter_dict = {}

for word in words:
    for char in word:
        
        if char not in letter_dict.keys():
            letter_dict[char] = 1
        else:
            letter_dict[char] += 1

letter_df = pd.DataFrame(letter_dict, index=[0]).T
letter_df = letter_df.sort_values(letter_df.columns[0], ascending=False)


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



def main():
    for iter in range(6):

        while True:
            try:
                guess = input('Enter guess: ')

                if guess.lower() == 'quit':
                    quit()
                elif len(guess) != 5:
                    raise ValueError
            except ValueError:
                print("Wordle guesses must be five letters long")
            
            else:
                break

        while True:
            try:
                result_of_guess = input('Enter result as a five letter string, where G is green, Y is yellow, and X is Grey: ')

                if len(result_of_guess) != 5:
                    raise ValueError
                if result_of_guess.lower() == 'ggggg':
                    print('Congratulations!')
            except ValueError:
                print("Results are the wrong length")
            
            else:
                break
            

    

        print(result_of_guess)

        guess = guess.lower()
        result_of_guess = result_of_guess.upper()


        words = wordle_utils.eliminate_words_based_on_guess(guess, result_of_guess, words)


        sorted_options = wordle_utils.find_options(words, n_options=7)

        if len(sorted_options) == 0:
            print('Sorry, we give up!')
            quit()

        print(f'Top 7 Options: {sorted_options} from {len(sorted_options)}')


if __name__ == '__main__':
    main()
