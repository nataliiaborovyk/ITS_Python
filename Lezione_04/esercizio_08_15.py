'''
8-15. Printing Models: Put the functions for the example printing_models.py 
in a separate file called printing_functions.py. Write an import statement 
at the top of printing_models.py, and modify the file to use the imported functions.
'''

print("\n   Esercizio 8-15")


# VERSIONE 1
print("\nVersione 1")

import Tools.functions_2 as utl    
utl.check_value(10)


# VERSIONE 2      
print("\nVersione 2")

from Tools.functions_2 import check_value

check_value(15)


# VERSIONE 3
print("\nVersione 3")

import Tools.functions_2

check_value(4)
