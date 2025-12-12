'''
 Domanda 1 (1.0 punti)
Calcola Fattoriale
Scrivi una funzione che calcola il fattoriale di un numero intero non negativo n (n!).
calculate_factorial(n: int) -> int

Requisiti:
Se n è negativo, la funzione deve sollevare un’eccezione ValueError con il messaggio esatto: "n negativo".

Non usare librerie (es. math.factorial).

Esempi:
Se n = 5, il calcolo è 5 * 4 * 3 * 2 * 1 = 120. La funzione restituisce: 120
Se n = 1, la funzione restituisce: 1
Se n = 0, (per definizione, 0! = 1) la funzione restituisce: 1

'''

def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n negativo")
    prod: int = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


def calculate_factorial2(n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * calculate_factorial2(n - 1)


'''
Domanda 2 (1.0 punti)
Logica di Controllo Allarme
Scrivi una funzione che simula un sistema di sicurezza basato su tre sensori: s1, s2, s3.
L’allarme si attiva solo se entrambe le seguenti condizioni sono vere:
Il sensore s1 è True.

I sensori s2 e s3 hanno stati diversi (uno True, l’altro False).

La funzione deve restituire la stringa "Allarme attivato" se le condizioni sono soddisfatte,
 altrimenti "Nessun allarme".
check_security_alarm(s1: bool, s2: bool, s3: bool) -> str


Esempi di input → output
s1=True, s2=True, s3=False → "Allarme attivato"
s1=True, s2=False, s3=True → "Allarme attivato"
s1=True, s2=True, s3=True → "Nessun allarme" (perché s2 e s3 non sono diversi)
s1=False, s2=True, s3=False → "Nessun allarme" (perché s1 è falso)
'''
def check_security_alarm(s1: bool, s2: bool, s3: bool) -> str:
    if s1 and s2 != s3:
        return "Allarme attivato"
    return "Nessun allarme"


'''
 Domanda 3 (1.0 punti)
Filtra Numeri e Concatena Stringa
Scrivi una funzione con il seguente header:
filter_and_concat(nums: list[int], min_val: int) -> str

La funzione riceve una lista di numeri interi (nums) e un valore intero (min_val).
 Deve restituire una stringa contenente tutti i numeri della lista che sono strettamente maggiori di min_val.
 I numeri nella stringa risultante devono essere separati da una virgola.

Esempio
Se
 nums = [10, 5, 20, 15, 3]  e min_val = 12,
 la funzione deve restituire:  "20,15"

Caso Particolare
Se
 nums = [1, 2, 3]  e  min_val = 5,
 la funzione deve restituire una stringa vuota:  ""
'''

def filter_and_concat(nums: list[int], min_val: int) -> str:
    lista: list[int] = []
    for el in nums:
        if el > min_val:
            lista.append(str(el))

    result: str = ",".join(lista)

    if len(lista) == 0:
        return ""
    return result
