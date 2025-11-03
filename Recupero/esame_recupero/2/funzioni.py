'''
Scrivi una funzione con il seguente header:
calculate_std_dev(nums: list[float]) -> float che, data una lista di numeri,
ritorni la deviazione standard (radice quadrata della varianza). Se la lista è vuota, solleva
un’eccezione ValueError con messaggio "lista vuota". Attenzione: non usare funzioni
built-in di python o librerie.
'''


def calculate_std_dev(nums:list[float]) -> float:
    if not nums:
        raise ValueError
    sum = 0
    for i in nums:
        sum += i
    media = sum/ len(nums)
    var = 0
    for i in nums:
        var += (i - media) ** 2
    varianza = var / len(nums)

    deviazione = varianza ** 0.5
    print(deviazione)

print(calculate_std_dev([1,2,3]))


'''
Scrivi una funzione che verifica se una combinazione di sensori (S1, S2, S3) attiva l'allarme.
L'allarme si attiva solo se S1 è vero e (S2 o S3 è falso). La funzione deve ritornare "Allarme
attivato" oppure "Nessun allarme" a seconda delle condizioni.
check_security_alarm(s1: bool, s2: bool, s3: bool) -> str
'''
def check_security_alarm(s1: bool, s2: bool, s3: bool) -> str:
    if s1 and (not s2 or not s3):
        return "allarme attivato"
    return "nessun allarme"


'''
filter_and_concat(nums: list[int], min_val: int) -> str che prenda una
lista di interi e un valore minimo, e restituisci una stringa concatenata di tutti i numeri di nums
che sono maggiori di min_val, separati da virgola (es. "5,7,9")
'''

def filter_and_concat(nums: list[int], min_val: int) -> str:
    lista:list = [str(x) for x in nums if x > min_val]
    return ",".join(lista)



