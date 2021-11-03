#################################################################
# FILE : hangman.py
# WRITER : eyal , eyalmutzary , 206910432
# EXERCISE : intro2cs ex4 2021
# DESCRIPTION: A great hangman game
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED: Wikipedia, W3School
# NOTES: ...
#################################################################

import hangman_helper
import copy

"""
Update the pattern based on the guessed letter
    :param word: the picked word
    :param pattern: the current pattern
    :param letter: the guessed letter
    :return: The updated pattern (string)
"""
def update_word_pattern(word, pattern, letter):
    pattern = list(pattern)
    if letter in word:
        for i in range(len(pattern)):
            if word[i] == letter:
                pattern[i] = letter
    return ''.join(pattern)


"""
returns the new score based on how many times the letter repeated
"""
def update_score(score, repetitions):
    return score + repetitions*(repetitions+1)//2


"""
checks if the guess is valid.
"""
def validate_guess(guess):
    return guess.islower() and len(guess) == 1 and guess.isalpha()


"""
Handles with a guess of letter
    :param game: dict of the current game stats
    returns an updated game stats
"""
def guessed_letter(game):
    if game["guess"] not in game["wrong_guesses"] \
            and game["guess"] not in game["pattern"]:
        game["score"] -= 1
        repetitions = game["word"].count(game["guess"])
        if repetitions != 0 and game["guess"] not in game["pattern"]:
            game["pattern"] = update_word_pattern(game["word"],
                                                  game["pattern"],
                                                  game["guess"])
            game["score"] = update_score(game["score"], repetitions)
        else:
            game["wrong_guesses"].append(game["guess"])
    else:
        game["msg"] = "You already picked that letter"
    return game


"""
Handles with a ask for clue
    :param game: dict of the current game stats
    :param word_list: a list of all the words
    prints a optional words as a clue
"""
def asked_for_clue(game, words_list):
    filtered_words = filter_words_list(words_list,
                                       game["pattern"],
                                       game["wrong_guesses"])
    if len(filtered_words) > hangman_helper.HINT_LENGTH:
        step = ((hangman_helper.HINT_LENGTH-1)*len(words_list)) \
              // hangman_helper.HINT_LENGTH
        clues = []
        for i in range(0,len(filtered_words),step):
            clues.append(filtered_words[i])

    game["score"] -= 1
    hangman_helper.show_suggestions(filtered_words)



"""
Runs a single round of the game
    :param word_list: a list of all the words
    :param score: the score the player starts with
    prints a optional words as a clue
"""
def run_single_game(words_list, score):
    game = {"word": hangman_helper.get_random_word(words_list),
            "pattern": "",
            "wrong_guesses": [],
            "msg": "",
            "guess": "",
            "guess_type": "",
            "score": score
            }
    game["pattern"] = '_' * len(game["word"])
    while '_' in game["pattern"] and game["score"] > 0:
        hangman_helper.display_state(game["pattern"],
                                     game["wrong_guesses"],
                                     game["score"],
                                     game["msg"])
        game["msg"] = ""
        game["guess_type"], game["guess"] = hangman_helper.get_input()
        if game["guess_type"] == hangman_helper.LETTER\
                and validate_guess(game["guess"]):
            guessed_letter(game)
        elif game["guess_type"] == hangman_helper.WORD:
            game["score"] -= 1
            if game["guess"] == game["word"]:
                game["score"] = update_score(game["score"],
                                             game["pattern"].count('_'))
                game["pattern"] = game["word"]
                break
        elif game["guess_type"] == hangman_helper.HINT:
            asked_for_clue(game, words_list)
        else:
            game["msg"] = "Wrong input!"
    if game["score"] != 0:
        game["msg"] = "Good job! You guessed the word!"
    else:
        game["msg"] = "Better luck next time! The word was \""\
                      + game["word"] + "\""
    hangman_helper.display_state(game["pattern"],
                                 list(game["wrong_guesses"]),
                                 game["score"],
                                 game["msg"])
    return game["score"]


"""
Inititate a new round
    :param round: the number of rounds the player did so far
    :param score: the score the player starts with
    prints a optional words as a clue
"""
def init_new_round(words_list, round=1, score=hangman_helper.POINTS_INITIAL):
    status = {"rounds": round, "score": score}
    status["score"] = run_single_game(words_list,
                                      status["score"])
    return status


"""
Initiate a new game
"""
def init_game(words_list):
    status = init_new_round(words_list)
    while status["score"] > 0: # => Won
        msg = "You played " + str(status["rounds"]) + \
              " rounds, and accumulated " + str(status["score"])
        if hangman_helper.play_again(msg):
            status = init_new_round(words_list, status["rounds"] + 1, status["score"])
        else:
            return
    msg = "Game over. You did " + str(status["rounds"]) + " rounds. "
    if hangman_helper.play_again(msg):
        init_game(words_list)


"""
Checks if a word is valid for clue
    :param word: the word that's being checked
    :param pattern: the current pattern
    :param wrong_guess_lst: the set of wrong guesses
    :returns True if word is valid
"""
def filter_word(word, pattern, wrong_guess_lst):
    if len(word) == len(pattern):
        for index, letter in enumerate(word):
            if letter in wrong_guess_lst:
                return False
            elif pattern[index] != '_' \
                    and word.count(letter) != pattern.count(letter):
                return False
            elif pattern[index] != '_' and letter == pattern[index]:
                continue
        return True
    return False



"""
Filters a whole list of words by the filter_word function
    :param words: a list of all the words
    :param pattern: the current pattern
    :param wrong_guess_lst: the set of wrong guesses
    :returns a list of the filtered words
"""
def filter_words_list(words_list, pattern, wrong_guess_lst):
    words = [word for word in words_list
             if filter_word(word,pattern,wrong_guess_lst)]
    return words


"""
Init the program
"""
def main():
    words_list = hangman_helper.load_words()
    init_game(words_list)


if __name__ == "__main__":
    main()
