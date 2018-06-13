a = "Jupiter"
print(a[1])

planet_name = "Neptune"
print(planet_name[::-1])

work_tip = "good code has meaningful variable names"
print("work_tip:", work_tip, "\n")
location = work_tip.find("o")
print(location)



# Mystery Name

first_name = input("Enter a first name: ")

for x in first_name :
    if x == "e" :
        x = "?"

new_name = first_name[::-1]
print(new_name)


# Words after "G"/"g"

quote = input("Enter a 1 sentence quote: ")
word = ""

for letter in quote :
    if letter.isalpha() :
        word += letter
    elif word[0] >= "h" :
        print(word.upper())

# letter to Number Function

phone_letters = [' ',"","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

def let_to_num() :
    letter = input("Enter a single letter, space, or empty string: ")
    key = 0
    while key < 10:
        if letter.lower() in phone_letters[key].lower() :
            print(key)
        else :
            key += 1
            print("Not Found")
let_to_num()

# Mystery name (영진)

# Mystery Name

first_name = input("Enter a first name: ").lower()
new_name=""

for x in first_name[::-1]:
    if x=="e":
        new_name+="?"
    elif x=="t":
        new_name+="?"
    elif x=="a":
        new_name+="?"
    else:
        new_name+=x

print(new_name)
