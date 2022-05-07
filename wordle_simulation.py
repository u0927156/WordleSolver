import wordle_solver_utils as wu
import random

def load_words():
    filename = './wordle-list-main/words'

    with open(filename) as file:
        words = file.readlines()
        words = [line.rstrip() for line in words]

    return words


def result_of_guess(guess, ground_truth):
    
    result = ''
    for i in range(len(guess)):
        guess_char = guess[i]

        if guess[i] == ground_truth[i]:
            result += 'g'
        elif guess_char in ground_truth:
            result += 'y'
        else:
            result += 'x'
        

    return result




def play_game(starting_guess, ground_truth, words):

    guess = starting_guess
    for iter in range(6):
        result = result_of_guess(guess, ground_truth)



        if result == 'ggggg':
            return iter + 1

        words = wu.eliminate_words_based_on_guess(guess, result, words)

        sorted_options = wu.find_options(words, n_options=7)

        guess = sorted_options[0]
    
    return -1


def run_simulation(n_sims, starting_guess):

    words = load_words()

    result_dict = {}
    for n in range(n_sims):
        ground_truth = random.choice(words)

        iterations = play_game(starting_guess, ground_truth, words)

        if iterations not in result_dict.keys():
            result_dict[iterations] = 1
        else:
            result_dict[iterations] += 1

    return result_dict
