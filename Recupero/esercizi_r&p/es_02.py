

# def is_integer(numero) -> bool:
#     if numero is int and numero > 0:
#         return True
#     return False

def numeri_interi_positivi():

    x = input("Inserici un numero intero positivo: ")
    if x.isdigit() and x > 0:
        x = float(x)
        if not x.is_integer():
            raise ValueError("Inserici un numero intero positivo ")
        else:
            x = int(x)
    else: 
        raise ValueError("Inserichi il numero intero")
    
    seguenza: list[int] = []
    while True:
        num = input("Inserici un numero intero positivo (\"0\" per terminare): ")
        if num.isdigit() and x > 0:
            num = float(num)
            if num.is_integer() and num != 0.0:
                seguenza.append(int(num))
            elif num.is_integer() and num == 0.0:
                seguenza.append(int(num))
                break
            else:
                raise ValueError(f"il numero inserito {num} non sodisfa la condizione")
        else:
            raise ValueError("Inserici il numero e non altro carattere")
    print(x)
    print(seguenza)

    cont:int = 0
    pos: list = []
    for i in range(len(seguenza)):
        if seguenza[i] == x:
            cont += 1
            pos.append(i)
    print(f"Numero {x} si incontra {cont} volte nel {seguenza}. La posozione del primo valore è {pos[0]}")

    
numeri_interi_positivi()
