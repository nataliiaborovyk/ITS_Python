'''
6-7. People: Start with the program you wrote for Exercise 6-1. 
Make two new dictionaries representing different people, 
and store all three dictionaries in a list called people. 
Loop through your list of people. As you loop through the list, 
print everything you know about each person.
'''

#esercizio_6-7
print(" \n   Esercizio_6-7\n")

first_dict: dict[str, str] = {
    "first_n": "Anna", 
    "last_n": "Bozi", 
    "age": '29', 
    "city": "Rome"}

second_dict: dict[str, str] = {
    "first_n": "Marco", 
    "last_n": "Rossi", 
    "age": '21', 
    "city": "Napoli"}

third_dict: dict[str, str] = {
    "first_n": "Stefano", 
    "last_n": "D'Omo", 
    "age": '32', 
    "city": "Milano"}
  
name_list: list[dict] = [first_dict, second_dict, third_dict]  
for i in name_list:
    print('')
    for k, v in i.items():
        print(f'{k}: {v}')