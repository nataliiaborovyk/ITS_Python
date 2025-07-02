'''
Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.

For example:  print(list_statistics([1, 2, 3, 4, 5]))
Test 	Result  (5, 1, 3.0)

'''
def list_statistics(numbers: list[int]) -> tuple:
    
    sum: float = 0
    
    for i in range(len(numbers)):
        sum += numbers[i]
        if i == 0:
            max:int = numbers[i]
            min:int = numbers[i]
        else:
            if numbers[i] > max:
                max = numbers[i]
            elif numbers[i] < min:
                min = numbers[i]
    
    media = sum / len(numbers)
    
    return max, min, media

print(list_statistics([1, 2, 3, 4, 5]))         #(5, 1, 3.0)
print(list_statistics([10, 20, 30, 40, 50]))    #(50, 10, 30.0)
print(list_statistics([-5, -1, -3]))            #(-1, -5, -3.0)
print(list_statistics([2]))                     #(2, 2, 2.0)
print(list_statistics([1, 1, 1, 1, 2]))         #(2, 1, 1.2)

