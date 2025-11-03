# Chiede all'utente di inserire una stringa
stringa:str = input("Digitare una stringa: ")

# Inizializza una stringa vuota per contenere la stringa invertita
reverse:str = ""

# Iterazione su ogni carattere della stringa
for char in stringa:
    # Aggiunge il carattere alla stringa invertita
    # Esempio: se la stringa è "ciao" e char è "c", la stringa invertita sarà "c" + ""
    # Se char è "i", la stringa invertita sarà "i" + "c"
    # E così via
    reverse = char + reverse

print(f"Stringa: {stringa}\nStringa invertita: {reverse}")