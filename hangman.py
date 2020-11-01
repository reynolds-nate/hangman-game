from random import randint

f = open('hangmanWords.txt')
wordList = f.read().splitlines()

f2 = open('alphabet.txt')
alphabet = f2.read().splitlines()

guessPartial=""
numGuess=0

for x in range(26):
    print(alphabet[x])

def selectWord(list):
    """
    selects word from list of words taken from imported document
    """
    
    word = list[randint(0,(len(list)-1))]

    return word

##def printBoard():



print("Hello, and Welcome to Hangman.")

while True:
    
    genWord=selectWord(wordList)

    
    guessPartial="_ "* len(genWord)

    print(genWord)
    print(guessPartial)

    while True:
        print("Your word is "+str(len(genWord))+" long.")
        print("You have guessed "+ str(numGuess) + " times and your progress is ")

        option = ("Guess a Letter.")
        break









    exitCon=input("exit? (Y/N)")
   
   #exit check
    print(exitCon)

    if exitCon == "Y":
        break







    
    

exit



