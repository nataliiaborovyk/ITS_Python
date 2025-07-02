'''
8-3. T-Shirt: Write a function called make_shirt() that accepts 
a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt 
and the message printed on it. Call the function once using positional arguments 
to make a shirt. Call the function a second time using keyword arguments.
'''

print("\n   Esercizio 8-3\n")

#function that eccepts a size and text of a message on T-shirt
def make_shirt(size: str, message: str):
    print(f"The size of t-shirt is: {size}\nThe message is: {message}\n")

#parameters passed by position
make_shirt("s", "sono carina!")

#parameters passed by keyword
make_shirt(message = "sono carina!!!", size = "s")