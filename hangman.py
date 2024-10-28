import random
from words import words

def get_word():
    word = random.choice(words)
    return word.upper()
