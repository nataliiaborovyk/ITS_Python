'''
2. Trova tutte le email in un testo
Scrivi una funzione extract_emails(text) che prende un testo e restituisce tutte le email trovate.
Esempio:
text = "Contattaci a info@azienda.com oppure support@help.org"
extract_emails(text)  # ['info@azienda.com', 'support@help.org']
'''

import re

def extract_emails(text:str) -> list:

    lista_email:list = re.findall(r'\w+@[A-Za-z0-9.]+\.[a-z]{2,}', text)

    print(lista_email)

text = "Contattaci a info@azienda.com oppure support@help.org"
extract_emails(text)  # ['info@azienda.com', 'support@help.org']