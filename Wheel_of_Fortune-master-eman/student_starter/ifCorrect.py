import random
import wordFunctions
import guessFunction
def ifCorrect(guess, total, Word, word, amount):
    for letter in range(len(guess)):
        if guess[letter] == word[letter]:
            if not Word[letter].isalpha():
                Word[letter] = guess[letter]
                if guess[letter] not in guessFunction.vowels and guess[letter].isalpha():
                    total += amount
    return total