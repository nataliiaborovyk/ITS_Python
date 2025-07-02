from string import punctuation
'''
Password Validation:  Write a function validate_password(password) that checks whether a password meets the following criteria: Minimum length of 20 characters, 
At least three uppercase letters, At least four special characters (non-alphanumeric). If the password is valid, the function should return True. 
If the password is invalid, the function should raise a built-in exception (e.g., ValueError) with a message indicating which criteria were not met.
'''

def validate_password(password:str):
    
    cont_1 = 0
    cont_2 = 0
    
    for i in password:
        if i.isupper():
            cont_1 += 1
        if i in punctuation:
            cont_2 += 1

    if len(password ) < 20:
        raise ValueError(f"Password \"{password}\" must have minimum length of 20 characters")
    
    
    if cont_1 < 3:
        raise ValueError(f"Password \"{password}\" must have at least three uppercase letters")
    
    if cont_2 < 4:
        raise ValueError(f"Password \"{password}\" must have at least four special characters (non-alphanumeric)")
    
    return True
    
try:
    print(validate_password("fvhdhvjhgbbbrbbtbrtrtj"))
except ValueError as error:
    print(error)
else:
    print("Your pasword is good")


try:
    print(validate_password("HGTFFjhdsc.,1£!!fcsdcsdcs"))
except ValueError as error:
    print(error)
else:
    print("Your pasword is good")

