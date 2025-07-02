'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.
'''

#esercizio 5-9
print("\n Esercizio 5-9 \n")

lista:list[str] = ["admin", "user", "Marco", "Federico"]

lista2:list = []

for i in lista:
    if i == "admin":
        print("Hello admin, would you like to see a status report?")
    elif i!= "admin":
        print(f"Hello {i}, thank you for logging in again.")
    

if lista2 == []:
    print("\nThe list is empty, we need to find some users!")  
