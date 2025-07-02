'''
8-5. Cities: Write a function called describe_city() 
that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. 
Give the parameter for the country a default value. 
Call your function for three different cities, 
at least one of which is not in the default country.
'''

print("\n   Esercizio 8-5\n")

#function that accepts the name of a city and its country
def describe_city(name:str, country:str="Italy"):
    print(f"La citta {name} si trova in {country}\n")

#parameters passed by position
describe_city("Reykjavik", "Iceland")

#only 1st parameter passed by position, 2nd by default
describe_city("Roma")

describe_city("Milano")

#parameters passed by keyword
describe_city(country="Francia", name="Paris")
