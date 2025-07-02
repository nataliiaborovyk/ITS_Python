'''
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user. 
Create several instances representing different users, and call both methods for each user.
'''
print("\n   Esercizio 9 -3")

class User:
    
    def __init__(self, first_name:str, last_name:str, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.kwargs = kwargs
        
    def describe_user(self):
        print(f"Name: {self.first_name}\nSurname: {self.last_name}")
        for k, v in self.kwargs.items():
            print(f"{k}: {v}")

    def greet_user(self):
        print(f"Hello {self.first_name}!")

user_1 = User("Nataliia", "Borovyk", corso="Data Analyst", citta="Roma")
user_1.describe_user()
user_1.greet_user()

print("")
user_2 = User("Chiara", "Macciochi", corso="Data Analyst", laurea="Economia", età=26)
user_2.describe_user()
user_2.greet_user()
    
