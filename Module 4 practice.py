order_c = input("Enter color : ")
order_s = input("Enter size : ")

if order_c.lower() == "white":
    if order_s.lower() == "l" or order_s.lower() == "m" :
        print("available")
    else :
        print("unavailable")
elif order_c.lower() == "blue":
    if order_s.lower() == "m" or order_s.lower() == "s" :
        print("available")
    else :
        print("unavailable")
else :
    print("unavailable")

