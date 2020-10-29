from random import randint

f = open('hangmanWords.txt')
wordList = f.read().splitlines()

def selectWord(list):
    """
    selects word from list of words taken from imported document
    """
    
    word = list[randint(0,(len(list)-1))]

    return word


print("Hello, and Welcome to Hangman.")

while True:
    
    genWord=selectWord(wordList)

    print(genWord)

    exitCon=input("exit? (Y/N)")
   
    print(exitCon)

    if exitCon == "Y":
        break







    
    

exit



