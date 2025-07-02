

class User:

    def __init__(self, first_name:str, last_name:str, email:str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        print(f"Name: {self.first_name}\nSurname: {self.last_name}\nEmail: {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name}!")


class Privileges:

    def __init__(self, lista:list):
        self.lista = lista

    def show_privileges(self):
        print(*self.lista, sep=", ")


class Admin:

    def __init__(self, user:User, privilege:Privileges):
        self.user = user
        self.privilege = privilege

    def describe_user(self):
        self.user.describe_user()

    def show_privileges(self):
        self.privilege.show_privileges()
