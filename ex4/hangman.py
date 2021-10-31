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


def run_single_game(words_list, score):
    word = hangman_helper.get_random_word(words_list)
    pattern = '_' * len(word)
    guesses = set()
    msg = ""
    while '_' in pattern and score > 0:
        hangman_helper.display_state(pattern, guesses, score, msg)
        guess_type, guess = hangman_helper.get_input()
        if guess_type == 1 and validate_guess(guess): # => Letter
            if guess not in guesses:
                guesses.add(guess)
                score -= 1
                repetitions = word.count(guess)
                if repetitions != 0:
                    pattern = update_word_pattern(word, pattern, guess)
                    score = update_score(score, repetitions)
            else:
                msg = "You already picked that letter"
        elif guess_type == 2: # => word
            score -= 1
            if guess == word:
                score = update_score(score, pattern.count('_')) - 1
                break
        elif guess_type == 3: # => Clue
            msg = "Clues are not supported yet."
        else:
            msg = "Wrong input!"
    if score != 0:
        msg = "Good job! You guessed the word!"
    else:
        msg = "Better luck next time! The word was \"" + word + "\""
    hangman_helper.display_state(pattern, guesses, score, msg)
    return score


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


def main():
    init_game()


if __name__ == "__main__":
    main()

