'''
Exercise 2
Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, 
or equal to 10 characters.
'''
print("\n   Esercizio 2\n")

#function that takes a string as an argument

def check_length(string:str):

    if len(string) > 10:
        print(f"\n La stringa \"{string}\" ha piu di 10 carratteri")

    elif len(string) < 10:
        print(f"\n La stringa \"{string}\" ha meno di 10 carratteri")
        
    else:
        print(f"\n La stringa \"{string}\" ha 10 carratteri")

check_length("sono al lezione")

check_length("mercoledi")

check_length("Ho fame!!!")