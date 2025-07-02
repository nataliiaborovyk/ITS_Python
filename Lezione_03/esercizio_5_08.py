'''
5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'.
 Imagine you are writing code that will print a greeting to each user after they 
 log in to a website. Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin,
 would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
'''

#esercizio 5-8
print("\n Esercizio 5-8 \n")

lista: list[str] = ["user", "admin", "Marco", "Federico"]

print("Lista:", *lista, '\n')


for i in lista:
    if i == "admin":
        print("Hello admin, would you like to see a status report?\n")
    else:
        print(f"Hello {i}, thank you for logging in again.")