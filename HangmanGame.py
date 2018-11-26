def makelist():
    filename = 'c:/work/fruits.txt'
    inputfile = open(filename)
    text = inputfile.read()
    inputfile.close()
    lst = text.split("\n")
    return lst

def displayHangMan(count):
    text = ["""
           +---+
               |
               |
               |
               |
               |
        -----------""",
        """
           +---+
           |   |
               |
               |
               |
               |
       -----------""",
        """
           +---+
           |   |
           O   |
               |
               |
               |
       -----------""",
        """
           +---+
           |   |
           O   |
          /    |
               |
               |
       -----------""",
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
       -----------""",
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
       -----------""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
       -----------""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
       -----------"""]
    
    print(text[count])
            

def randomword(lst):
    import random
    number = random.randint(0,len(lst)-1)
    word = lst[number].lower()
    return word

def guessword(word):
    import random
    hiddenword = word
    randalpha = word[random.randint(0,len(word)-1)]
    for letter in hiddenword:
        if letter != randalpha:
            hiddenword = hiddenword.replace(letter,"_")
    print(hiddenword)
    return hiddenword


def inputguess():
    guess = input("Enter a guess: ").lower()
    return guess

def change_hiddenword(guess,word,hiddenword):
    new_hiddenword = ""
    i = 0
    for letter in hiddenword:
        if letter == "_":
            if word[i] == guess:
                new_hiddenword += guess
            else:
                new_hiddenword += letter
        else:
            new_hiddenword += letter
        i+=1
    return new_hiddenword
        

def runGame():
    lst = makelist()
    word = randomword(lst)
    deathcount = 0
    displayHangMan(deathcount)
    hiddenword = guessword(word)
    guesshistory = ""
    print(guesshistory)
    while deathcount < 7 and hiddenword != word:
        guess = inputguess()
        if not guess.isalpha():
            print("Incorrect input")
        elif guess in guesshistory:
            print("Incorrect input")
        elif guess not in word:
            guesshistory += guess
            deathcount += 1
            displayHangMan(deathcount)
            print(hiddenword)
            print(guesshistory)
        elif guess in word :
            guesshistory += guess
            displayHangMan(deathcount)
            new_hiddenword = change_hiddenword(guess,word,hiddenword)
            hiddenword = new_hiddenword
            print(hiddenword)
            print(guesshistory)
    if hiddenword == word:
        print("Congratulation\nYou saved the hangman!")
    if deathcount == 7:
        print("Hangman died...T_T\nThe answer is",word)

runGame()
