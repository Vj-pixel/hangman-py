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
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion="".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha(): # checks if the guess is a word and it is a alphabetic letter
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word")
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry you ran out of tries. The word was " + word + ". Maybe next time!")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again? (y/n) ").upper == "Y":
    word = get_word()
    play(word)

if __name__ == "__main__":
    main()
