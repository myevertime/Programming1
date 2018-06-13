# Module 4 practice - pi guessing

!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi -o pi.txt

pi = open("pi.txt",'r')
print(pi.read())

name = input("Enter your name:")
seed = len(name)
pi.seek(seed)
digit = pi.read(1)
if digit == "." :
    seed += 1
    pi.seek(seed)
    digit = pi.read(1)
elif digit == "\n" :
    seed += 1
    pi.seek(seed)
    digit = pi.read(1)
correct = 0
wrong = 0
guess = input("Enter a single digit guess or \"q\"to quit: ")
while guess != "q" :
    if guess.isdigit() is True :
        if guess == digit :
            correct += 1
        elif guess != digit :
            wrong += 1
    guess = input("Enter a single digit guess or \"q\"to quit: ")
print(correct, wrong)
