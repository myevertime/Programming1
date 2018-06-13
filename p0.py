def grillSteak(steakTemp, targetTemp, increaseAmount):
    while steakTemp < targetTemp:
        steakTemp = steakTemp + increaseAmount
        print('Current steak temperature is', steakTemp)
    return steakTemp

finalSteakTemp = grillSteak(94, 155, 13)
print('Final steak temperature is', finalSteakTemp)


import math
math.sqrt(81)
math.ceil(8.1)
math.floor(8.9)
round(8.5)
round(8.5)
math.pi

import random
random.randint(0,3)
random.randint(0,3)
random.randint(0,3)

import datetime
datetime.date.today()
datetime.date.today()
datetime.date.today()

import winsound
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

import webbrowser
webbrowser.open('https://www.python.org/')

import math
def distance(x1,y1,x2,y2):
    distance = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
    return distance

print('Distance:', distance(2,1,10,8))

