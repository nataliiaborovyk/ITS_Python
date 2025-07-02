'''
8-13. User Profile:  Build a profile of yourself by calling build_profile(), 
using your first and last names and three other key-value pairs that describe you. 
All the values must be passed to the function as parameters. 
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
'''

print("\n   Esercizio 8-13\n")

# VERSIONE 1
print("\n Versione 1")

def build_profile(first_name:str, last_name:str, **kwargs):

    output: str = f"{first_name} {last_name}, "
    counter: int = 0

    for key, value in kwargs.items():
        output += f"{key}: {value}"  
        
        if counter < len(kwargs) - 1:
            output += ", "
        counter += 1
        
    return output

print(build_profile("Eric", "Crow", age=45, hair="brown", weight=72))



# VERSIONE 2
print("\n Versione 2")

def build_profile(first_name:str, last_name:str, **kwargs):

    output: str = f"\n{first_name} {last_name}, "
    counter: int = 0

    for key, value in kwargs.items():
        output += f"\n{key}: {value}"  
        
    return output


print(build_profile("Eric", "Crow", age=45, hair="brown", weight=72))