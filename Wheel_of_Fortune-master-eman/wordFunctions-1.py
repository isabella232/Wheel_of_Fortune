import random

from random import randint
def getWord():
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
    s=(categories[list(categories.keys())[category]][
    randint(0, (len(list(categories[list(categories.keys())[category]])) - 1))]).upper()
    return s

def printWord(word):
    for char in word:
        print(char, end=' ')
    print()