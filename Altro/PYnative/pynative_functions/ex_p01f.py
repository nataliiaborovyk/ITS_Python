'''
Exercise 1: Create a function in Python
Write a program to create a function that takes two arguments, 
name and age, and print their value.
'''
# versione 1
print("\nversione 1")

def date(name: str, age: int) -> dict[str, int]:
    return {"Name":name, "age": age}

user= date("Tom", 40)
print("Name: ",user["Name"], "Age: ",user["age"])


# versione 2
print("\nversione 2")

def date_2(name:str, age:int):
    print(f"Name: {name} and age: {age}")

date_2("Alice", 25)


# versione 3
print("\nversione 3")

def date_3(**kwargs) -> dict[str, int]:
    for name, age in kwargs.items():
        print(f"{name}: {age}", end=" ")
    print("")
    return {"Name": name, "Age": age}
  
print(date_3(name="Tom", age=40))
