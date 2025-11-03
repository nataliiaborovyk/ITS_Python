pi:float = 4.0 # inizio della serie
i:int = 1 # contatore dei termini della serie

# ciclo per calcolare pi
while round(pi,2)!=3.14:
    # termini pari della serie
    if i % 2 == 0:
        pi = pi + (4/(2*i +1))
    # termini dispari della serie
    else:
        pi = pi - (4/(2*i +1))

    # aggiorna il contatore dei termini
    i = i + 1

# stampa il numero di termini necessari per approssimare pi greco a 3.14
print(f"Per approssimare pi greco a 3.14 occorrono {i} termini della serie!")


pi:float = 4.0 # inizio della serie
i:int = 1 # contatore dei termini della serie

# ciclo per calcolare pi
while round(pi,3)!=3.141 :
    # termini pari della serie
    if i % 2 == 0:
        pi = pi + (4/(2*i +1))
    # termini dispari della serie
    else:
        pi = pi - (4/(2*i +1))

    # aggiorna il contatore dei termini
    i = i + 1

# stampa il numero di termini necessari per approssimare pi greco a 3.141
print(f"Per approssimare pi greco a 3.141 occorrono {i} termini della serie!")  


pi:float = 4.0 # inizio della serie
i:int = 1 # contatore dei termini della serie

# ciclo per calcolare pi
while round(pi,4)!=3.1415:
    # termini pari della serie
    if i % 2 == 0:
        pi = pi + (4/(2*i +1))
    # termini dispari della serie
    else:
        pi = pi - (4/(2*i +1))

    # aggiorna il contatore dei termini
    i = i + 1

# stampa il numero di termini necessari per approssimare pi greco a 3.1415
print(f"Per approssimare pi greco a 3.1415 occorrono {i} termini della serie!")  



pi:float = 4.0 # inizio della serie
i:int = 1 # contatore dei termini della serie

# ciclo per calcolare pi
while round(pi,5)!=3.14159:
    # termini pari della serie
    if i % 2 == 0:
        pi = pi + (4/(2*i +1))
    # termini dispari della serie
    else:
        pi = pi - (4/(2*i +1))
        
    # aggiorna il contatore dei termini
    i = i + 1
    
# stampa il numero di termini necessari per approssimare pi greco a 3.14159
print(f"Per approssimare pi greco a 3.14159 occorrono {i} termini della serie!")