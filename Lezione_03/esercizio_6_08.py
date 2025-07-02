'''
6-8. Pets: Make several dictionaries, where each dictionary represents 
a different pet. In each dictionary, include the kind of animal and 
the owner’s name. Store these dictionaries in a list called pets. Next, 
loop through your list and as you do, print everything you know about each pet.
'''

#esercizio_6-8
print(" \n   Esercizio_6-8\n")

asia_dict: dict[str, str] = {
    "animal": " cat",
    "name": "Asia", 
    "owner's_name": "Alex",
    "gender": "female",
    "color": "brown",
    "age": "12"}

lilu_dict: dict = {
    "animal": " dog",
    "name": "Lilu", 
    "owner's_name": "Natallia",
    "gender": "female",
    "color": "panna",
    "age": '7'}

tancredi_dict: dict = {
    "animal": " cat",
    "name": "Tancredi", 
    "owner's_name": "Rita",
    "gender": "male",
    "color": "wight",
    "age": "9"}

pets_list: list[dict] = [asia_dict, lilu_dict, tancredi_dict]
for i in pets_list:
    print('')
    for k, v in i.items():
        print(f'{k}: {v}')

