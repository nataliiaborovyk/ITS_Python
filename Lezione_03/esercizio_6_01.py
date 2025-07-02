'''
6-1. Person: Use a dictionary to store information about a person you know. 
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name, last_name, age, and city. 
Print each piece of information stored in your dictionary.
'''

#esercizio_6-1
print(" \n   Esercizio_6-1\n")

mydict: dict[str, str] = { "first_name": "Anna", 
"last_name": "Bozi", "age": '29', "city": "Rome"}
for k, v in mydict.items():
    print(f'{k}: {v}')