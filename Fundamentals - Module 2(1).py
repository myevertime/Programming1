# Fundamentals - Module 2(1)

def city_search(search_items, cities = ["New York","Shanghai", "Munich","Tokyo"])
    for city in cities :
        if city.lower() == search_item.lower():
            return True
        else :
            pass

    return False

visited_cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico Cities"]
search= input("enter a city visited: ")
print()

print(search.title(), "in default cities is", city_search(search))
print(search.title(), "in visited cities list is", city_search(search, visited_cities))
