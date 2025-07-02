def nome(x, y:int = 1, *args, **kwargs):
    for k, v in kwargs.items():
        if k == "chiave1":
            print(v)
        elif k == "chiave2":
            print(v)
        else:
            raise ValueError("Chiave non riconosciuta")
            print("parametro non riconosciuto")
    print(x, y, args, kwargs)

#nome(1,2,chiave1=9)

def nome2(dataclass) -> None:
    dataclass.nome
    dataclass.cognome
    dataclass.data_nascita

nome(x = 10)