def get_names() :
    element_list = []
    count = 0
    while count < 5 :
        element_names = input("Enter the name of element: ")
        if element_names == "" :
            continue
        elif element_names not in element_list :
            element_list.append(element_names)
            count += 1
    return element_list

print(get_names())


