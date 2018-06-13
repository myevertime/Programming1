# String Methods

start = 0
quote = "they stumble who run fast"
space_index = quote.find(" ")

while space_index != -1 :
    print(quote[start:space_index])
    start = space_index
    space_index = quote.find(" ", space_index +1)
    
