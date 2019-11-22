import random
import wordFunctions
import guessVowels


def removeAlphabet(str_list, guess,amount ):
    str_list.remove(guess, amount)
    for char in range(len(Word)):
        if word[char] == guess:
            Word[char] = guess
            total += amount
    print('You have: $' + str(total))
    wordFunctions.printWord(Word)

   # str=input("Hello world or fuck you world?")
    #printOutput(str)

    #def printOutput(response):
     #   print "The user wishes to say"
      #  print response
