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
        if len(guess) == 1 and guess.isalpha():


        elif len(guess) == len(word) and guess.isalpha():

        else:
            print("Not a valid guess")
