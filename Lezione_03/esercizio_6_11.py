'''
6-11. Cities: Make a dictionary called cities. Use the names of three cities 
as keys in your dictionary. Create a dictionary of information about each city 
and include the country that the city is in, its approximate population, 
and one fact about that city. The keys for each city’s dictionary should be 
something like country, population, and fact. Print the name of each city 
and all of the information you have stored about it.
'''

#esercizio_6-11
print(" \n   Esercizio_6-11")

city_dict: dict[str, dict[str, str]] = {
    "Roma": {
        "country":"Italy",
        "popolation": "2.76 million",
        "monuments": "Colosseo"
        },
    "Paris": {
        "country":"France",
        "popolation": "2,1 million",
        "monuments": "Eiffel Tower"
        },
    "Berlin": {
        "country":"German",
        "popolation": "3,44 million",
        "monuments": "Branderbuge Gate"
        }
    }

for i in city_dict:    
    print(f"\n  City {i}")
    for k, v in city_dict[i].items():
        print(f"{k.capitalize()}: {v}")


# versione 2
print("\nversione2\n")

for i, k in city_dict.items():
    country = k["country"].title()
    population =  k["popolation"]
    monuments = k["monuments"].title()

    print(f"\n{i.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The monumet famouse is {monuments}.")

