from random import randint

f = open('hangmanWords.txt')
wordList = f.read().splitlines()

f2 = open('alphabet.txt')
alphabet = f2.read().splitlines()

guessPartial=""
numGuess=0
guessedLetters = []

for x in range(26):
    print(alphabet[x])

def selectWord(list):
    """
    selects word from list of words taken from imported document
    """
    
    word = list[randint(0,(len(list)-1))]

    return word

##def printBoard(numGuesses, guessPartial):

def getLetter():
     while True:
        letter = input('Enter a letter:').upper()
        try:
            (letter.isalpha && ((len(letter))==1) && (guessedLetters.find(letter)==-1))
        except:
            if(!(letter.isalpha && ((len(letter))==1))):
                print('Please enter a letter A-Z.')
            if(!(guessedLetters.find(letter)==-1)):
                print("You've already guessed that letter.")
            continue
    
        break
 



def gameMenu()



print("Hello, and Welcome to Hangman.")

while True:
    
    genWord=selectWord(wordList)

    
    guessPartial="_ "* len(genWord)

    print(genWord)
    print(guessPartial)

    while True:
        print("Your word is "+str(len(genWord))+" long.")
        print("You have guessed "+ str(numGuess+1) + " times and your progress is ")

        option = input("Guess a Letter.")
        guessedLetters.append(option)
        
        print(guessedLetters[numGuess])








        break









    exitCon=input("exit? (Y/N)")
   
   #exit check
    print(exitCon)

    if exitCon == "Y":
        break







    
    

exit



