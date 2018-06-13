# Fundamentals - Module 3 - End of Assignment / Poem Mixer

words_list = input("enter a poem, verse or saying: ")
new_list = words_list.split(" ")


for letter in new_list :
        if len(letter) <= 3 :
            new_list[new_list.index(letter)] = letter.lower()
        elif len(letter) >= 7 :
            new_list[new_list.index(letter)] = letter.upper()
        else :
            pass

new_list.sort()
new_words = []

while len(new_list) > 5 :
    new_words.append(new_list.pop(-5))
    new_words.append(new_list.pop(0))
    new_words.append(new_list.pop(-1))

print(new_words)



