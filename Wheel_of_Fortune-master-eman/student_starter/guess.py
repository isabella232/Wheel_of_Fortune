# Keep guessing until word is guessed correctly
def guessFuntion():
   while True:
        while True:
            # Pick an random amount from amounts
            amount = amounts[randint(0, (len(amounts) - 1))]
            guess = input().upper()
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