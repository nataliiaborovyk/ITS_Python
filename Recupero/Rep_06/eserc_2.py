
def listaNomi():
    lista_nomi:list[str] = []
    max = ""
    while True:
        nome:str = input()
        if nome == "":
            print("Il nome non puo essere stringa vuota")
        elif len(nome) > 20:
            print("Il nome deve essere entro 20 caratteri")
        elif nome in lista_nomi:
            break
        elif len(lista_nomi) >30:
            break
        else:
            lista_nomi.append(nome)
            if len(nome) > len(max):
                max = nome
    print(f" Erano inseriti {len(lista_nomi)} \nIl nome {max} è piu lungo di tutti e ha {len(max)} carrateri")

listaNomi()



