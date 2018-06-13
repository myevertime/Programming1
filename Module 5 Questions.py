def adding_report(phrase):
    print("Input an integer to add to the total or \"Q\"to quit")
    items = ""
    total = 0
    report = ""
    while report != "Q" :
        report = input("Enter an integer or \"Q\" : ")
        if report.isdigit() :
            if phrase == "A" :
                items += "\n" + report
                total += int(report)
            elif phrase == "T" :
                total += int(report)
                print("Total \n", "\n" ,total)
        elif report.lower() == "q" :
            print("Items\n",items, "\n Total", "\n", total)
            break
        else :
            print(report," is invalid input")
            

adding_report("A")
adding_report("T")
