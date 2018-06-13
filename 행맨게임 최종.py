import random

def displayHangMan(number):
    if number==0:
        print(format('+---+','^20'))
        i=0
        while i<5:
            print(format('|','>12'))
            i+=1
        print(format('-'*11,'>14'))
    elif number==1:
        print(format('+---+','^20'))
        print(format('|   |','>12'))
        i=0
        while i<4:
            print(format('|','>12'))
            i+=1
        print(format('-'*11,'>14'))
    elif number==2:
        print(format('+---+','^20'))
        print(format('|   |','>12'))
        print(format('O   |','>12'))
        i=0
        while i<3:
            print(format('|','>12'))
            i+=1
        print(format('-'*11,'>14'))
    elif number==3:
        print(format('+---+','^20'))
        print(format('|   |','>12'))
        print(format('O   |','>12'))
        print(format('/    |','>12'))
        i=0
        while i<2:
            print(format('|','>12'))
            i+=1
        print(format('-'*11,'>14'))
    elif number==4:
        print(format('+---+','^20'))
        print(format('|   |','>12'))
        print(format('O   |','>12'))
        print(format('/|   |','>12'))
        i=0
        while i<2:
            print(format('|','>12'))
            i+=1
        print(format('-'*11,'>14'))
    elif number==5:
        print(format('+---+','^20'))
        print(format('|   |','>12'))
        print(format('O   |','>12'))
        print(format('/|\\  |','>12'))
        i=0
        while i<2:
            print(format('|','>12'))
            i+=1
        print(format('-'*11,'>14'))
    elif number==6:
        print(format('+---+','^20'))
        print(format('|   |','>12'))
        print(format('O   |','>12'))
        print(format('/|\\  |','>12'))
        print(format('/    |','>12'))
        i=0
        while i<1:
            print(format('|','>12'))
            i+=1
        print(format('-'*11,'>14'))
    elif number==7:
        print(format('+---+','^20'))
        print(format('|   |','>12'))
        print(format('O   |','>12'))
        print(format('/|\\  |','>12'))
        print(format('/ \\  |','>12'))
        i=0
        while i<1:
            print(format('|','>12'))
            i+=1
        print(format('-'*11,'>14'))

            
def randomword(lst):
    number=random.randint(0,len(lst))
    word=lst[number]
    return word

def gamestart(lst):
    Deathcount=0
    displayHangMan(Deathcount)
    Answer=randomword(lst)
    wordlength=len(Answer)
    Disp='_'
    guessword='' 
    startword=Answer[random.randint(0,wordlength-1)].lower()
    i=0
    while i<wordlength:
        if Answer[i].lower()==startword:
            guessword=guessword+startword
        else:
            guessword=guessword+Disp
        i+=1
    Disp=guessword
    print(guessword)
    guesslist=''
    while guessword!=Answer.lower() and Deathcount<7:
        IncorInp=False
        totalcount=0
        guess=input('Enter a guess: ')
        guessword=''
        if guess in Answer.lower() and guess not in guesslist:
            while totalcount<wordlength:
                if Answer[totalcount].lower()==guess:
                    guessword=guessword+guess
                else:
                    guessword=guessword+Disp[totalcount]
                totalcount+=1
            Disp=guessword
            guesslist=guesslist+guess
        elif guess in guesslist or len(guess)>1:
            IncorInp=True
        elif not guess.isalpha():
            IncorInp=True
        else:
            Deathcount+=1
            guesslist=guesslist+guess
        if IncorInp:
            print('Incorrect Input')
        else:
            displayHangMan(Deathcount)
            print(Disp)
            print(guesslist)
    if guessword==Answer.lower():
        print('Congratulations!')
        print('You saved the hangman!')
    else:
        print('Hangman died T.T')
        print('The answer is', Answer.lower())
    
    
filename='c:/work/fruits.txt'
inputfile=open(filename)
text=inputfile.read()
lst=text.split('\n')
inputfile.close()

gamestart(lst)

