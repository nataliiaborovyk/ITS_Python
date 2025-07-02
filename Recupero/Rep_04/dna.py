
import re

def dna_sovrapposizione():
    while True:
        s1 = input("Inserisci la prima sequenza: ").upper()
        s2 = input("Inserisci la seconda sequenza: ").upper()
        if re.fullmatch(r"[ACGT]+", s1) and re.fullmatch(r"[ACGT]+", s2):
            break
        else:
            print("Errore: una o entrambe le sequenze non sono valide. Riprova.\n")

    len_min = min(len(s1), len(s2))
    sovrapp = 0
    for i in range(len_min, 0, -1):
        if s1[-i:] == s2[:i]:
            sovrapp = i
            break

    print("\nStringhe sovrapposte:")
    print(s1)
    print(" " * (len(s1) - sovrapp) + s2)
    print(f"\nLa massima lunghezza di sovrapposizione è {sovrapp}.")

dna_sovrapposizione()
