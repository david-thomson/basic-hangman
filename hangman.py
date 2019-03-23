import random, re, sys, os

# Open word file and randomly select a word to play the game with
gameDictionary = open("words.txt", "r")
data = gameDictionary.read()
words = data.split(" ")
numWords = len(words)
gameWordIndex = random.randint(0,(numWords - 2))
gameWord = words[gameWordIndex] #The actual word used for the game
gameWord = gameWord.upper()

usedChars = [""]
gameWordStatus = "_ " * len(gameWord)
correctGuesses = 0
line1 = r"___________"
line2 = r"|          "
line3 = r"|          "
line4 = r"|            "
line5 = r"|            "
line6 = r"|"
line7 = r"|"
line8 = " "




# Function to replace the blank characters with correctly guessed chars
def correctGuess(index, guess):
    global gameWordStatus
    global correctGuesses
    correctGuesses += 1
    tempStatus = gameWordStatus[0:(index)] + str(guess.upper()) + gameWordStatus[(index + 1)::]
    gameWordStatus = tempStatus

# Function to "Add" each part to the hangman drawing
def incorrectGuess(guessesTaken):
    global line2
    global line3
    global line4
    global line5
    if guessesTaken == 1:
        line2 = r"|         |"
    elif guessesTaken == 2:
        line3 = r"|         0"
    elif guessesTaken == 3:
        line4 = r"|         |  "
    elif guessesTaken == 4:
        line4 = r"|        /|  "
    elif guessesTaken == 5:
        line4 = r"|        /|\ "
    elif guessesTaken == 6:
        line5 = r"|        /   "
    elif guessesTaken == 7:
        line5 = r"|        / \ "
#        print("Game over, you lose")

# Function to display the hangman
def hangMan():
    os.system('clear')
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)
    print(line8)

def drawGame():
    os.system('clear')
    hangMan()
#    print(gameWord) # testing purposes only to show the solution
    print(" ")
    print(gameWordStatus[0::])

guessesTaken = 0
while guessesTaken < 7:
    drawGame()
    line8 = ""
    print("Take a guess. " + str(7 - guessesTaken) + " guesses remaining")
    print("Already used: " + str(usedChars[1::]))
    guess = str(input())
    if not re.match("^[a-z]*$", guess):
        line8 = "Error! Only letters a-z allowed!"
        continue
    elif len(guess) > 1:
        line8 = "Error! Only 1 character allowed!"
        continue
    elif guess.upper() in usedChars:
        line8 = "Error! You have already used this character!"
        continue
    guess = guess.upper()
    if guess.upper() in gameWord:
        line8 = "Correct!"
        usedChars.append(guess.upper())
        for i in range(len(gameWord)):
            if gameWord[i] == guess.upper():
                correctCharIndex = i * 2
                correctGuess(correctCharIndex, guess)
        if correctGuesses == len(gameWord):
            hangMan()
            print(gameWordStatus[0::])
            print("Congratulations, you won!")
            break
    elif guess.upper() not in gameWord:
        line8 = "Incorrect, try again"
        print(gameWordStatus)
        usedChars.append(guess)
        guessesTaken += 1
        incorrectGuess(guessesTaken)
        hangMan()
        print(guessesTaken)
else:
    line8 = "The word was: " + gameWord
    hangMan()
    print("Game over, you lose")
    sys.exit()

# To do list:
# - Clean remaining code
