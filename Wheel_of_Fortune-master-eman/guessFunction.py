import random
import wordFunctions 

from random import randint

# List of letters to remove after each guess
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


# List of all vowels
vowels = ['A', 'E', 'I', 'O', 'U']

def guessfunction(Word ,word, amounts):
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
                        wordFunctions.printWord(Word)
                        break
                    if '_' not in Word:
                        wordFunctions.printWord(Word)
                        print('You have: $' + str(total))
                        break
                    else:
                        for char in range(len(Word)):
                            if word[char] == guess:
                                Word[char] = guess
                    print('$' + str(total))
                    wordFunctions.printWord(Word)
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
                wordFunctions.printWord(Word)
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
                wordFunctions.printWord(Word)
                if '_' not in Word:
                                    break
        # If word or phrase is fully guessed, end game
        if '_' not in Word:
            print('You won!')
            break