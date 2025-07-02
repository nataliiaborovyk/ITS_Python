'''
Esercizio 3C-8. Scrivere un programma in Python che legga una frase di una riga e mostri una delle seguenti risposte:
- "Si" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è pari;
- "No" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è dispari;
- "Wow!" -> se la frase termina con un punto esclamativo (!)
- "Tu dici" seguito dalla frase inserita racchiusa tra doppi apici in tutti gli altri casi.
'''

print("\n Esercizio 3C-8\n")

frase:str = input("Inserisci una frase: ")

lungezza:int = len(frase)
print(f"\nLa tua frase ha {lungezza} caratteri")

match frase:
    case frase if lungezza % 2 == 0 and frase[-1] == "?":
        print(f"\nSi")
    case frase if lungezza % 2 != 0 and frase[-1] == "?":
        print(f"\nNo")
    case frase if frase[-1] == "!":
        print(f"\nWow!")
    case _:
        print(f"\n{frase} \"Tu dici\"\n")