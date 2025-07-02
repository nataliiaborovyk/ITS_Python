'''
 Imported Admin: Create a module users.py containing three classes:
    User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
    Privileges: holds a list of privileges and a method show_privileges() to display them.
    Admin: stores a User instance and a Privileges instance as attributes.
In a separate file main.py, import the classes, create a User and a Privileges instance, pass them to Admin, 
and call describe_user() and show_privileges() to verify everything works correctly.
'''

from esercizio_09_11_users import User
from esercizio_09_11_users import Privileges
from esercizio_09_11_users import Admin

user_1: User = User("Nataliia", "Borovyk", "nataliiaborovyk@gmail.com")
priv_1:Privileges = Privileges(["puo modificare il contenuto", "puo condividre il contenuto"])
adm_1:Admin = Admin(user_1, priv_1)

adm_1.describe_user()
adm_1.show_privileges()