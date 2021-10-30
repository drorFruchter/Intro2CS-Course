def update_word_pattern(word, pattern, letter):
    pattern = list(pattern)
    if letter in word:
        for i in range(len(pattern)):
            if word[i] == letter:
                pattern[i] = letter
    return ''.join(pattern)


def update_score(score, repetitions):
    return score + repetitions*(repetitions+1)//2


def validate_guess(guess, word_len):
    if guess.islower() and len(guess) == 1 and guess.isalpha():
        return "letter"
    elif len(guess) == word_len:
        return "word"
    else:
        return "invalid"


def run_single_game(words_list=["hello", "world"], score=0):
    word = "hello" # need to call get_random_word()
    pattern = '_' * len(word)
    guesses = set()
    while '_' in pattern:
        print(pattern) #Call desplay state
        guess = input("Enter letter") # Call get_input()
        guess_type = validate_guess(guess, len(word))
        if guess_type == "letter":
            if guess not in guesses:
                guesses.add(guess)
                score -= 1
                repetitions = word.count(guess)
                if repetitions != 0:
                    pattern = update_word_pattern(word, pattern, guess)
                    score = update_score(score, repetitions)
            else:
                print("You already picked that letter")
        elif guess_type == "word":
            score = update_score(score, pattern.count('_')) - 1
            break
        else:
            print("Wrong input!")
    print("Success! The word was: " + word)
    print("You finished with " + str(score) + " points!")
