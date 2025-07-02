'''
Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) 
è soddisfatta per procedere con un'operazione. 
L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni 
che sono soddisfatte.
print(check_combination(True, False, True))   Result  Operazione permessa
print(check_combination(False, True, False))          Operazione negata
'''

# VERSIONE 1

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    # cancella pass e scrivi il tuo codice
    if conditionA == True and conditionB == True or conditionC == True:
        return "Operazione permessa"
    elif conditionA != True and conditionB == True and conditionC == True:
        return "Operazione permessa"
    else:
        return "Operazione negata"
    
print(check_combination(True, False, True))  #Operazione permessa
print(check_combination(False, True, True))   #Operazione permessa
print(check_combination(False, True, False))  #Operazione negata
print(check_combination(True, True, True))    #Operazione permessa
print(check_combination(False, False, False))   #Operazione negata
    



# VERSIONE 2

def check_combination_2(conditionA: bool, conditionB: bool, conditionC: bool) -> str:

    if conditionA == True or (conditionC == True and conditionB == True):
        return f"Operazione permessa"
    
    return f"Operazione negata"

print("")
print(check_combination_2(True, False, True))  #Operazione permessa
print(check_combination_2(False, True, True))   #Operazione permessa
print(check_combination_2(False, True, False))  #Operazione negata
print(check_combination_2(True, True, True))    #Operazione permessa
print(check_combination_2(False, False, False))   #Operazione negata

