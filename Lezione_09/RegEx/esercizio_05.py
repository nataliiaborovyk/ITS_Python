'''
5. Estrai tutte le date nel formato gg/mm/aaaa
Scrivi una funzione find_dates(text) che trova tutte le date in formato italiano (dd/mm/yyyy) in un testo.
Esempio:
text = "Le date importanti sono 09/04/2025 e 15/08/2023."
find_dates(text)  # ['09/04/2025', '15/08/2023']
'''

import re
def find_dates(text):
    list_dates:list = re.findall(r'((?:0[1-9]|[1-2][0-9]|3[0-1])/(?:0[1-9]|1[0-2])/(?:\d{4}))', text)
    print(list_dates)

text = "Le date importanti sono 09/04/2025 e 15/08/2023."
find_dates(text)  # ['09/04/2025', '15/08/2023']



# def find_dates(text):
#     list_dates:list = re.findall(r'((0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/(\d{4}))', text)
#     for i in list_dates:
#         print(i[0])

# text = "Le date importanti sono 09/04/2025 e 15/08/2023."
# find_dates(text)  # ['09/04/2025', '15/08/2023']



def find_dates(text):
    for i in re.finditer(r'((0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/(\d{4}))', text):
        print(i.group(0))

text = "Le date importanti sono 09/04/2025 e 15/08/2023."
find_dates(text)  # ['09/04/2025', '15/08/2023']
