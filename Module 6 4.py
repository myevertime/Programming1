# Fundamentals _ Module 1 end of assignment

quote = input("Enter a input: ")
word = ""

for x in quote :
    if x.isalpha() :
        word += x
    else :
        if word.lower() >= "h":
            print(word.upper())
            word = ""
        else :
            word = ""
