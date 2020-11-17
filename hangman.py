from random import randint

f = open('hangmanWords.txt')
wordList = f.read().splitlines()

f2 = open('alphabet.txt')
alphabet = f2.read().splitlines()

for i in range(26):
    alphabet[i] = alphabet[i].upper()

numGuess=0 #number of guesses made
guessedLetters = [] #letters that have been guessed
currentGuess="" #the current letter being guessed
secretWord=""

for x in range(26):
    print(alphabet[x])

def selectWord(list):
    """
    selects word from list of words taken from imported document
    """
        
    word = list[randint(0,(len(list)-1))]

    return word
    
def validLetter(currentGuess): 
   

    if (currentGuess.isalpha()) and currentGuess.upper() not in guessedLetters:
        return True
    else:
        return False

def getLetter():
    while True:
        print("Enter a letter.")
        currentGuess=input()
        if validLetter(currentGuess):
            guessedLetters[guessNum]=currentGuess
            return currentGuess


def updatePartial(letter):
    if letter is in secret:
        guessPartial[secret.index(letter)]
        secretWord = selectWord(wordList)
secret=list(secretWord)

print(secretWord)
print(secret)

guessNum=0
playing = True
while playing :
    letter = getLetter()

    break

print(letter)
    
