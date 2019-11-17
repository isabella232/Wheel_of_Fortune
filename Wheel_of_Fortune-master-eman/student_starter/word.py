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