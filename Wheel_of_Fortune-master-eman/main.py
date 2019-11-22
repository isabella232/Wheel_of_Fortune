# Rules
import random
import wordFunctions
import guessFunction

print(
    'Guess one letter at a time. If you want to buy a vowel, you must have at least $500, otherwise, you cannot buy a vowel. If you think you know the word or phrase, type \'guess\' to guess the word or phrase. You will earn each letter at a set amount and vowels will not cost anything.')

from math import ceil
from random import randint

# needed for your test cases so your random outputs would match ours
random.seed(3)

amounts1 = [500, 750, 1000, 1250, 1500, 1750, 5000]
total = 0

# Get a random word or phrase from the category
word1 = wordFunctions.getWord()


# word = input().upper()
# Fill up list with blanks for characters in word
Word1 = []
for char in word1:
    if char.isalpha():
        Word1.append('_')
    else:
        Word1.append(char)


# Function to print Word

wordFunctions.printWord(Word1)

# Keep guessing until word is guessed correctly
guessFunction.guessfunction(Word1,word1,amounts1)
