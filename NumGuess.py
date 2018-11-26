import random

def inputUserGuess():
    userGuess = int(input('Take a guess: '))
    while userGuess < 0 or userGuess > 100:
        print('Wrong guess')
        userGuess = int(input('Take a guess: '))
    return userGuess

computerGuess = random.randint(0,100)
userGuess = inputUserGuess()

while userGuess != computerGuess:
    if userGuess < computerGuess:
        print('Too low')
    else:
        print('Too high')
    userGuess = int(input('Take a guess: '))

print('You got it!')
    
