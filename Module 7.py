# Module 2 - Practice / letter to Number Function

def let_to_num() :
    phone_letters = [' ',"","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
    letter = input("Enter a single letter, space, or empty string: ")
    key = 0
    while key < 10 :
        if letter == "" :
            return 1
            break
        elif letter.lower() in phone_letters[key].lower() :
            return key
        else :
            key += 1
    return("Not found")
print(let_to_num())


# Module 2 - Practice / reverse

some_numbers = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77]
new_string = []

while len(some_numbers) != 0 :
    pop_num = some_numbers.pop(0)
    new_string.insert(0,pop_num)

print(new_string)


# Module 2 - End of Assignment

set_list = ["fish", "trees", "books", "movies", "songs"]


while len(set_list) != 0 :
    string = input("Enter a string or \"quit\" if you wanna quit: ")
    if string.lower() == "quit" :
        break
    else :
        def list_o_matic() :
            if string == "" :
                set_list.pop()
                print("pop msg")
            elif string in set_list :
                set_list.remove(string)
                print("remove msg")
            else :
                set_list.append(string)
                print("append msg")
        list_o_matic()
