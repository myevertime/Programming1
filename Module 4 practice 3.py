def ticket_check() :
    section = input("enter a section : (there is general and floor)")
    seats = input("enter seats : (there are 1 to 10)")
    seats_string = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
    if section.lower() == "general" :
        if seats.isdigit() is True :
            if seats in seats_string :
                print("True")
            else :
                print("False")

ticket_check()
