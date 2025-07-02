'''
8-14. Cars: Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. 
It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, 
such as a color or an optional feature. Your function should work for a call like this one: 
car = make_car('subaru', 'outback', color='blue', tow_package=True) 
Print the dictionary that’s returned to make sure all the information was stored correctly. 
'''

print("\n   Esercizio 8-14\n")

# VERSIONE 1
print("\n Versione 1")

def make_car(manufacturer: str,  model_name: str, **kwargs):
    output:str = f"{manufacturer}, {model_name},"
    counter:int = 0

    for key, value in kwargs.items():
        output += f" {key}: {value}"
        
        if counter < len(kwargs) - 1:
            output += ", "
        counter += 1
    #print(*kwargs)

    return output

print(make_car("subaru", "outback", color="blue", price=20000))


# VERSIONE 2
print("\n Versione 2")

def make_car(manufacturer: str,  model_name: str, **kwargs) -> dict:

    car: dict = {"Manufacturer": manufacturer, "Model": model_name}
    car.update(kwargs)

    return car

car:dict = make_car("subaru", "outback", color="blue", price=20000)
for k, v in car.items():
    print(f"{k}: {v}")

