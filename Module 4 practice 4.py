def str_analysis() :
    enter = input("please enter any sentence: ")
    while enter == "" :
        enter = input("please enter any sentence or number: ")
    if enter.isalpha() is True :
        print('"', enter,'"' , 'is all alphabetical characters!')
    elif enter.isdigit() is True :
        print("number")

str_analysis()
