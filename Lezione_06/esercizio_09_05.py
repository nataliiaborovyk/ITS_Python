'''
Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
Print login_attempts again to make sure it was reset to 0.
'''

class User:
    
    def __init__(self, first_name:str, last_name:str, login_attempts:int = 0, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.kwargs = kwargs
        
    def describe_user(self):
        print(f"Name: {self.first_name}\nSurname: {self.last_name}")
        for k, v in self.kwargs.items():
            print(f"{k}: {v}")

    def greet_user(self):
        print(f"Hello {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = User("Nataliia", "Borovyk", corso="Data Analyst", citta="Roma")
user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"{user_1.first_name} had done {user_1.login_attempts} login attemps" )

user_1.reset_login_attempts()
print(user_1.login_attempts)