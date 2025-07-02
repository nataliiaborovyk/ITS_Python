from string import ascii_lowercase

def cifrarioDiCesare(s: str, key: int) -> str:

    lettere:str = ascii_lowercase
    if key > 26:
        key = key % 26
    frase_nuova:str = ""
    s = s.lower()
    for i in range(len(s)):
        if s[i] in lettere:
            posiz = lettere.index(s[i])
            posiz1 = (posiz + key) % 26
            new_carat = lettere[posiz1]
            frase_nuova += new_carat
        else:
            frase_nuova += s[i]

    return frase_nuova

if __name__ == "__main__":
    print(cifrarioDiCesare("ciao!", 2))
    print(cifrarioDiCesare("ciao!", 28))

    print(cifrarioDiCesare("ekcq!", -2))

    print(cifrarioDiCesare("ciao!", 200)) #per criptare
    print(cifrarioDiCesare("uasg!", -200)) #per decriptare

    
    
    