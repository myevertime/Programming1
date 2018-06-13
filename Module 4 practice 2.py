def str_analysis() :
    analysis = input("enter: ")
    if analysis.isdigit() is True :
        if int(analysis) > 99 :
            print("big number")
        else :
            print("small number")
    elif analysis.isdigit() is False :
        if analysis.isalpha() is True :
            print("all alpha")
        elif analysis.isalpha() is False :
            print("being neither all alpha nor all digit")

str_analysis()
