from random import randint

# Getting a list of letters and words from preset text files
#all words and letters are put into lists as lowercase
f = open('hangmanWords.txt')
wordList = f.read().splitlines()

f2 = open('alphabet.txt')
alphabet = f2.read().splitlines()

#SHOW WORD PROGRESS
# Each round the word is displayed (e.g. Word: __mm_t)
# Guessed letters are unmasked.
# Hidden letters are shown as underscores.

def wordProgress():
    for  i in secret:
        if secret[i] in guessedLetters:
            progress += str(secret[i])
            progress += ' '
        else:
            progress += '_'
            progress += ' '

    progress = progress.strip()
    return progress

#SHOW REMAINING GUESSES
# Each round display the number of chances remaining.
# Display Chances remaining: CHANCES where CHANCES is an integer.

#GUESS LETTER OR WORD
# When a player enters a single character, it guesses a letter.
# When a player enters more than a single character, it guesses the word.

#CHECK GUESSED LETTERS
# If the guessed letter is within the word, those letters are unveiled.
# Display the number of times the letter is found when it is present.
# If the guessed letter is not within the word, subtract one from the chances remaining.
# The user is alerted if the guess is not found.
# If the guessed letter was already submitted, do not decrement the chances remaining.
# Display an error message if the letter was already guessed.

#CHECK GUESSED WORD
# If the guessed word matches the hidden word, the player wins the game.
# Output a congratulatory message if the guess was correct.
# If the guessed word does not match the hidden word, the player loses the game.
# Output an apologetic message if the guess was incorrect.

#GAME OVER WHEN NO MORE CHANCES
# The game ends when the number of chances remaining reaches zero.
# The user is alerted that they have run out of guesses


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


def updatePartial(letter, guessPartial):
    if letter in secret:
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
    
