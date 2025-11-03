# Chiede all'utente di inserire una stringa
stringa:str = input("Digitare una stringa: ")
# Inizializza un contatore di caratteri spazio
char_counter:int = 0

# Iterazione su ogni carattere della stringa
for i in range(len(stringa)):
    # Controlla se un carattere della stringa sia uguale al carattere di spazio " "
    if stringa[i] == " ":
        # Incrementa di uno il contatore di caratteri spazio
        char_counter += 1

print(f"Nella stringa:\n\"{stringa}\"\nci sono {char_counter} spazi!")