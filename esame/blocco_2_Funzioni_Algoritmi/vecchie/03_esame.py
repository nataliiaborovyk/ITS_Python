'''
Filtra e Concatena Numeri - PUNTI 1
Scrivi una funzione con il seguente header:
filter_and_concat(nums: list[int], min_val: int) -> strche prenda una
lista di interi e un valore minimo, e restituisci una stringa concatenata di tutti i numeri di nums
che sono maggiori di min_val, separati da virgola (es. "5,7,9").
Calcola Deviazione Standard - PUNTI 1
Scrivi una funzione con il seguente header:
calculate_std_dev(nums: list[float]) -> float che, data una lista di numeri,
ritorni la deviazione standard (radice quadrata della varianza). Se la lista è vuota, solleva
un’eccezione ValueError con messaggio "lista vuota". Attenzione: non usare funzioni
built-in di python o librerie.calculate_std_dev(nums: list[float]) -> float che, data una lista di
numeri, ritorni la deviazione standard (radice quadrata della varianza). Se la lista è vuota,
solleva un’eccezione ValueError con messaggio "lista vuota". Attenzione: non usare funzioni
built-in di python o librerie.
Nota Bene: Il calcolo della varianza misura la dispersione dei dati rispetto alla media. Si
calcola come la media dei quadrati delle differenze tra ciascun valore all’interno della lista e
la media dei valori della lista di numeri
Esempio:
Se nums = [1.0, 2.0, 3.0, 4.0, 5.0]:
1. Calcolo della media:
(1.0 + 2.0 + 3.0 + 4.0 + 5.0) / 5 = 15.0 / 5 = 3.0
2. Calcolo della varianza:
((1.0 - 3.0)^2 + (2.0 - 3.0)^2 + (3.0 - 3.0)^2 + (4.0 - 3.0)^2 + (5.0 - 3.0)^2) / 5
= ((-2.0)^2 + (-1.0)^2 + (0.0)^2 + (1.0)^2 + (2.0)^2) / 5
= (4.0 + 1.0 + 0.0 + 1.0 + 4.0) / 5
= 10.0 / 5 = 2.0
3. Calcolo della deviazione standard:
radice quadrata di 2.0 ≈ 1.41421356
Controllo Sicurezza - PUNTI 1
Scrivi una funzione che verifica se una combinazione di sensori (S1, S2, S3) attiva l'allarme.
L'allarme si attiva solo se S1 è vero e (S2 o S3 è falso). La funzione deve ritornare "Allarme
attivato" oppure "Nessun allarme" a seconda delle condizioni.
check_security_alarm(s1: bool, s2: bool, s3: bool) -> str
'''