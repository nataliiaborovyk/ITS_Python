
'''
Esercizio 3C-7. Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" 
o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".
NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.
'''

#Esercizio 3C-7
print("\n Esercizio 3C-7\n")

cont_t:int = 0
cont_c:int = 0
print("Inserisci il risultato del lancio di una moneta( \"t\" se uscita la \"testa\" o \"c\" se uscito il \"croce\"):   \n")

for i in range(1, 9):

    risultato:str = input(f"Lancio {i}: ")

    match risultato:
        case "t":
            cont_t += 1
        case "c":
            cont_c += 1
        case _:
            print("\nErrore, no riconosco il risultato")

    

percentuale_t = (cont_t * 100) / 8

percentuale_c = (cont_c * 100) / 8


print(f"\nTotale \"testa\": {cont_t}\nPercentuale \"testa\": {percentuale_t}")

print(f"\nTotale \"croce\": {cont_c}\nPercentuale \"croce\": {percentuale_c}\n")
