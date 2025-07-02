#function that takes a number as an argument

#print("perche stampa anche questa stringa che sta fuori dalla funzione?")

def check_value(n):

    if n > 5:
        print(f"Numero {n} > 5")

    elif n < 5:
        print(f"Numero {n} < 5")
        
    else:
        print(f"Numero {n} = 5")


'''
check_value(10)

check_value(3)

check_value(5)'''