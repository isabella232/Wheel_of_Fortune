# Rules
print(
    'Guess one letter at a time. If you want to buy a vowel, you must have at least $500, otherwise, you cannot buy a vowel. If you think you know the word or phrase, type \'guess\' to guess the word or phrase. You will earn each letter at a set amount and vowels will not cost anything.')

from math import ceil
from random import randint

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
word = (categories[list(categories.keys())[category]][
    randint(0, (len(list(categories[list(categories.keys())[category]])) - 1))]).upper()

# word = input().upper()
# Fill up list with blanks for characters in word
Word = []
for char in word:
    if char.isalpha():
        Word.append('_')
    else:
        Word.append(char)


# Function to print Word
def printWord(word):
    for char in word:
        print(char, end=' ')
    print()


printWord(Word)

# List of all vowels
vowels = ['A', 'E', 'I', 'O', 'U']

# Keep guessing until word is guessed correctly
while True:
    while True:
        # Pick an random amount from amounts
        amount = amounts[randint(0, (len(amounts) - 1))]
        print('$' + str(amount), 'per correct letter')
        print('$500 per vowel')
        guess = input().upper()
        # If the user wants to guess phrase or word
        if guess == 'GUESS':
            while True:
                correct = 0
                guess = input().upper()
                for letter in range(len(guess)):
                    if guess[letter] == word[letter]:
                        correct += 1
                    else:
                        break
                if correct == len(guess):
                    for letter in range(len(guess)):
                        if guess[letter] == word[letter]:
                            if not Word[letter].isalpha():
                                Word[letter] = guess[letter]
                                if guess[letter] not in vowels and guess[letter].isalpha():
                                    total += amount
                else:
                    print('Sorry, that\'s not the answer! Keep guessing!')
                    printWord(Word)
                    break
                if '_' not in Word:
                    printWord(Word)
                    print('You have: $' + str(total))
                    break
                else:
                    for char in range(len(Word)):
                        if word[char] == guess:
                            Word[char] = guess
                print('$' + str(total))
                printWord(Word)
                if '_' not in Word:
                    break
            break
        # If user guesses letter they've already guessed
        elif guess not in alphabet:
            print('You\'ve already picked that letter!')
            print('You have: $' + str(total))
        # If guess is a vowel, subtract $500 from total per vowel
        elif guess in vowels:
            if total >= 500:
                alphabet.remove(guess)
                for char in range(len(Word)):
                    if word[char] == guess:
                        total -= 500
                        Word[char] = guess
            # If user cannot buy vowel
            else:
                print('Not enough money')
            print('You have: $' + str(total))
            printWord(Word)
            if '_' not in Word:
                break
        # If everythin else is False, remove letter from alphabet and replace char in Word with letter in word
        else:
            alphabet.remove(guess)
            for char in range(len(Word)):
                if word[char] == guess:
                    Word[char] = guess
                    total += amount
            print('You have: $' + str(total))
            printWord(Word)
            if '_' not in Word:
                break
    # If word or phrase is fully guessed, end game
    if '_' not in Word:
        print('You won!')
        break
