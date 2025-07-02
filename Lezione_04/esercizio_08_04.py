'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts 
are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, 
and a shirt of any size with a different message.
'''

print("\n   Esercizio 8-3\n")

#function that eccepts a size and text of a message on T-shirt
def make_shirt(size = "L", message = "I love Python"):
    print(f"The size of t-shirt is: {size}\nThe message is: {message}\n")

#change only size
make_shirt("S")

make_shirt("M")

#change only message
make_shirt(message="I like your size")

