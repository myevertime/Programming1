# Mystery Name (안영진씨)

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



