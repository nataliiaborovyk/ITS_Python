'''
8. Trova parole con lettere maiuscole e numeri
Scrivi una funzione find_codes(text) che trova tutte le parole lunghe 8 caratteri, con lettere maiuscole e numeri.
Esempio:
text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
find_codes(text)  # ['AB12CD34', '12345678']
'''

import re

def find_codes(text):
    list_code:list = re.findall(r'(?=(?:.*[A-Z]){1})(?=(?:.*\d){1})[A-Z0-9]{8}', text)  
    print(list_code)

text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
find_codes(text)  # ['AB12CD34', '12345678']