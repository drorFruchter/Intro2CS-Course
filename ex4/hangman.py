import hangman_helper

WORDS_LIST = hangman_helper.load_words()

# Update a pattern based on the word and the letter it gets
# Returns the new pattern
def update_word_pattern(word, pattern, letter):
    pattern = list(pattern)
    if letter in word:
        for i in range(len(pattern)):
            if word[i] == letter:
                pattern[i] = letter
    return ''.join(pattern)


def update_score(score, repetitions):
    return score + repetitions*(repetitions+1)//2


def validate_guess(guess):
    return guess.islower() and len(guess) == 1 and guess.isalpha()


def guessed_letter(game):
    if game["guess"] not in game["wrong_guesses"] \
            and game["guess"] not in game["pattern"]:
        game["score"] -= 1
        repetitions = game["word"].count(game["guess"])
        if repetitions != 0 and game["guess"] not in game["pattern"]:
            game["pattern"] = update_word_pattern(game["word"], game["pattern"], game["guess"])
            game["score"] = update_score(game["score"], repetitions)
        else:
            game["wrong_guesses"].add(game["guess"])
    else:
        game["msg"] = "You already picked that letter"
    return game


def asked_for_clue(game, words_list):
    filtered_words = filter_words_list(words_list,
                                       game["pattern"],
                                       game["wrong_guesses"])
    if len(filtered_words) > hangman_helper.HINT_LENGTH:
        cut = (hangman_helper.HINT_LENGTH-1)*len(filtered_words) \
              // hangman_helper.HINT_LENGTH
        filtered_words = filtered_words[cut:cut+3]
    hangman_helper.show_suggestions(filtered_words)


def run_single_game(words_list, score):
    game = {"word": hangman_helper.get_random_word(words_list),
            "pattern": "",
            "wrong_guesses": set(),
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
        game["guess_type"], game["guess"] = hangman_helper.get_input()
        if game["guess_type"] == 1 and validate_guess(game["guess"]):
            guessed_letter(game)
        elif game["guess_type"] == 2:
            game["score"] -= 1
            if game["guess"] == game["word"]:
                game["score"] = update_score(game["score"],
                                             game["pattern"].count('_')) - 1
                break
        elif game["guess_type"] == 3: # => Clue
            asked_for_clue(game, words_list)
        else:
            game["msg"] = "Wrong input!"
    if game["score"] != 0:
        game["msg"] = "Good job! You guessed the word!"
    else:
        game["msg"] = "Better luck next time! The word was \""\
                      + game["word"] + "\""
    hangman_helper.display_state(game["pattern"],
                                 game["wrong_guesses"],
                                 game["score"],
                                 game["msg"])
    return game["score"]


def init_new_round(round=1, score=hangman_helper.POINTS_INITIAL):
    status = {"rounds": round, "score": score}
    status["score"] = run_single_game(WORDS_LIST,
                                      status["score"])
    return status


def init_game():
    status = init_new_round()
    while status["score"] > 0: # => Won
        msg = "You played " + str(status["rounds"]) + \
              " rounds, and accumulated " + str(status["score"])
        if hangman_helper.play_again(msg):
            status = init_new_round(status["rounds"] + 1, status["score"])
        else:
            return
    msg = "Game over. You did " + str(status["rounds"]) + " rounds."
    if hangman_helper.play_again(msg):
        init_game()


def filter_word(word, pattern, wrong_guess_lst):
    if len(word) == len(pattern):
        for index, letter in enumerate(word):
            if letter in wrong_guess_lst:
                return False
            elif pattern[index] != '_' and word.count(letter) != pattern.count(letter):
                return False
            elif pattern[index] != '_' and letter == pattern[index]:
                continue
        return True
    return False


def filter_words_list(words, pattern, wrong_guess_lst):
    words = filter(lambda word:
                   filter_word(word, pattern, wrong_guess_lst), words)
    return list(words)


def main():
    init_game()


if __name__ == "__main__":
    # main()
    run_single_game(["aaa"], 3)