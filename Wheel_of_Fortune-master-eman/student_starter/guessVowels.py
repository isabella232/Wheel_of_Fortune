import random
import wordFunctions
from random import randint
def guessVowels(total, Word, alphabet, guess, word):
    if total >= 500:
        alphabet.remove(guess)
        for char in range(len(Word)):
            if word[char] == guess:
                total -= 500
                Word[char] =- guess
    return Word[char]