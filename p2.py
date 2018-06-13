import math
def calcConeVolume(radius, height):
    v = (math.pi * (radius ** 2) * height) / 3
    return v

radius = int(input("Enter radius of a cone: "))
height = int(input("Enter height of a cone: "))
print("The volume is", calcConeVolume(radius, height))
