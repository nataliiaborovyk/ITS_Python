'''
Esercizio 1.

In biologia molecolare, le molecole di DNA possono essere viste come stringhe sull’alfabeto dei nucleotidi
A = adenina, C = citosina, G =guanina, T = timina.

Ad esempio: DNA: CAGCTGATCGATGCTAGCCTG.

Scrivere un programma in linguaggio Python che legge dall’utente due stringhe s1 e s2 corripondenti a frammenti di
DNA e verifica se s2 puo' essere sovrapposta su s1 in modo che una parte iniziale (prefisso) di s2 coincida con
una parte finale (suffisso) di s1.
 
Il programma dovra' dare la lunghezza della massima sovrapposizione (0 se non si possono sovrapporre).
 
Ad esempio, se l’utente ha inserito:
s1= CAGCTGATCGATGCTAGCCTG
s2= AGCCTGTTGCACCTAGA

Le due stringhe si sovrappongono come segue:
CAGCTGATCGATGCTAGCCTG
                                  AGCCTGTTGCACCTAGA

Il programma dovra' quindi stampare in output:

    le stringhe sovrapposte come nell'esempio.

    La massima lunghezza di sovrapposizione e' 6.


NOTA1:
il programma dovra' anche verificare la correttezza dell’input, ovvero le stringhe inserite dall’utente devono essere effettivamente frammenti di DNA.
Suggerimento: scrivere una funzione isDNA() che, data in input una sequenza, restituisca True se la sequenza passata è una valida sequenza del DNA formata dai soli caratteri A, C, G o T, e che restituisca False altirmenti.
Può essere utile usare una regex.

Nota2: trovare una soluzione che eviti di scrivere codice replicato per inizializzare le sequenze s1 e s2.

Infine, verificare le seguenti coppie di frammenti di DNA:
- s1= TTGACCAGGTCA
- s2= AACCGGTTAA
La massima lunghezza è 1

- s1= GGTACCGTGA
- s2= CGTGAACCTT
La massima lunghezza è 5

- s1= AAGCTTACG
- s2= ACGTTCGA
La massima lunghezza è 3

- s1= TTACGAGTACGCTAGT
- s2= ACGCTAGTCCGA
La massima lunghezza è 8
 
- s1= AGCTAACG
- s2= AACGTTCGA
La massima lunghezza è 4
 
- s1= AAAA
- s2= AAAA
La massima lunghezza è 4
 
- s1= ACGT
- s2= ATGC
La massima lunghezza è 0
 
Esercizio 2.

Si vuole calcolare la somma di tutti i prodotti x * y per tutti i valori interi di x (i cui valori variano tra 0 e 100) e tutti i valori interi di y (i cui valori sono dati dalla sequenza 2, 4, 6, 8, 10, 12, ..., 88), ovvero i prodotti
1 * 2,
1 * 4,
...
1 * 88,
2 * 2,
2 * 4,
...
2 * 88,
...
100 * 2,
100 * 4,
...
100 * 88

Scrivere una funzione Python proDict() che senza ricevere alcun argomento in input, che restituisce un dizionario che abbia come chiavi la tupla (x,y) e come valore x*y , in cui memorizzare tutti i prodotti x * y per tutti i valori interi di x e tutti i valori interi di y.

Nel main, scrivere un codice Python che inizializzi un dizionario d ricorrendo alla funzione prodDict e stampare in output i valori del dizionario d, per i seguenti valori di x e y:

    x = 13, y = 88

    x = 83, y = 56

    x = 71, y = 44


'''