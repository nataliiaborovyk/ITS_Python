'''
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
Call the function, making sure to include a book title as an argument in the function call.
'''

print("\n   Esercizio 8-2\n")

#function that print a message
def favorite_book(title:str):
    print(f"One of my favorite books is {title}")

favorite_book("Alice in Wonderland")