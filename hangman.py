import random
from words import words

def get_word():
    word = random.choice(words)
    return word.upper()


def play(word):
    word_completion = "_" * len(word) #number of _'s multiplied by the length of the word
    guessed = False #false until user guesses it
    guessed_letters = []
    guessed_words = []
    tries = 6 # 2 arms, head, 2 legs, body
    print("Let's play hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    # while loop below is when it's not guessed and tries are greater than 0
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper() #converts it to uppercase cuz that's how hangman works!
        # if-else block
        if len(guess) == 1 and guess.isalpha(): # checks if the guess is a letter and one character
            if guess in guessed_letters: #checks to see if the letter was already guessed
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1 # subtract total tries by 1
                guessed_letters.append(guess) # adds it to the guessed_letters array 👆
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)

        elif len(guess) == len(word) and guess.isalpha(): # checks if the guess is a word and it is a alphabetic letter

        else:
            print("Not a valid guess")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")
