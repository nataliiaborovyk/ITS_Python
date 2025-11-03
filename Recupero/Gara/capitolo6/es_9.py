'''
Tesoreria Ottimale
Segnala problema

Per gli apprendisti, misura l’esborso più efficiente.
 Realizza `min_coins(amount, coins)` restituendo il conteggio minimo,
   o `1000000000` quando non componibile.
 Mantieni la firma e promuovi i test.
'''

def min_coins(amount: int, coins: list[int]) -> int:
    coinSort:list[int] = sorted(coins,reverse=True)
    resto: int = amount
    cont: int = 0

    for i in coinSort:
        div = resto // i 
        if div > 0:
            resto = resto - (i * div)    
            cont += div

        if resto <= 0: # per non iterare inutilmente
            break
    if resto != 0:
        return 1000000000
    return cont



def min_coins(amount: int, coins: list[int]) -> int:
    # Inizializzo la tabella dei minimi
    INF = 1000000000
    dp = [INF] * (amount + 1)
    dp[0] = 0  # per fare 0 servono 0 monete

    # Riempio la tabella
    for somma in range(1, amount + 1):
        for valoreMoneta in coins:
            if valoreMoneta <= somma:
                dp[somma] = min(dp[somma], dp[somma - valoreMoneta] + 1)

    # Se dp[amount] è rimasto INF, la somma è impossibile
    return dp[amount]
