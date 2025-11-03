'''
Labirinto di Fibonacci

Per risvegliare il golem di Fibonacci registra in un grimorio 
i risultati parziali: usa `fib_memo(n)` per ottenere l'ennesimo numero
 evitando di rifare gli stessi passaggi. 
Mantieni la firma e titola i test.
'''

def fib_memo(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_memo(n-1) + fib_memo(n-2)