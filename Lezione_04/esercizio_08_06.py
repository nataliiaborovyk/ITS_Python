'''
8-6. City Names: Write a function called city_country() 
that takes in the name of a city and its country. 
The function should return a string formatted like this: 
"Santiago, Chile". Call your function with at least three 
city-country pairs, and print the values that are returned.
'''

print("\n   Esercizio 8-6\n")

#function that accepts the name of a city and its country
def city_country(city:str, country:str):
    #stringa = "\"" + city + "," + " " + country + "\""   -  un altra versione come scrivere codice
    return f"{city} is in {country}"

print(city_country("Roma", "Italy"))

mystring = city_country("Porto", "Portugal")
print(mystring)