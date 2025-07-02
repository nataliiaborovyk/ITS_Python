'''
6. Verifica un codice prodotto
Scrivi una funzione check_product_code(code) che verifica se il codice è nel formato PROD-1234-AB.
Esempio:
check_product_code("PROD-9876-ZX")  # True
check_product_code("PROD-99-ZX")    # False
'''

import re
def check_product_code(code):
    match = re.fullmatch(r'PROD-\d{4}-[A-Z]{2}', code)
    if match:
        print(True)
    else:
        print(False)   

check_product_code("PROD-9876-ZX")  # True
check_product_code("PROD-99-ZX")    # False