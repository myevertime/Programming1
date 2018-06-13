# Fundamentals - Module2(2) Task4 / List of letters

word = input("enter a word: ")
word_fin = int(word.count("")) -1
odd_letters = ""
even_letters = ""

for x in range(0,word_fin,2) :
    odd_letters = word[x]
    print(odd_letters)

for y in range(1,word_fin,2) :
    even_letters = word[y]
    print(even_letters)

# Fundamentals - Module 2(3) Task 7 / add the digits

string = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
new_string = string.split()
total = 0

for letter in new_string :
    total += int(letter)

print("The result of ", "+".join(new_string), "is", total)
