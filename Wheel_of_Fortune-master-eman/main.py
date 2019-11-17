# Rules
import random
import guess
import word
print(
    'Guess one letter at a time. If you want to buy a vowel, you must have at least $500, otherwise, you cannot buy a vowel. If you think you know the word or phrase, type \'guess\' to guess the word or phrase. You will earn each letter at a set amount and vowels will not cost anything.')

from math import ceil
from random import randint

# needed for your test cases so your random outputs would match ours
random.seed(3)

amounts = [500, 750, 1000, 1250, 1500, 1750, 5000]
total = 0


# List of letters to remove after each guess
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
# Categories and words
categories = {'color': ['red', 'green', 'blue', 'yellow', 'turqouise', 'purple', 'indigo', 'white', 'black'],
                'phrase': ["it's raining cats and dogs", "speak of the devil", "the best of both worlds",
                    "see eye to eye", "when pigs fly", "costs an arm and a leg", "once in a blue moon",
                    "a piece of cake", "let the cat out of the bag", "feeling under the weather",
                    "kill two birds with one stone"]}
# Pick a random category
category = randint(0, (len(categories) - 1))
# Print category name
print('Category:', list(categories.keys())[category])
# Get a random word or phrase from the category


printWord(Word)

# List of all vowels
vowels = ['A', 'E', 'I', 'O', 'U']

print('$' + str(amount), 'per correct letter')
print('$500 per vowel')
guessFunction()  