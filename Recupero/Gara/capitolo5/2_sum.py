'''
Torce Pari

Per tarare il banco servono misure con parità perfetta: 
usa `count_even(nums)` per contare quanti valori sono **pari** (compreso `0`). 
Mantieni la firma e promuovi i test.
'''

def count_even(nums: list[int]) -> int:
    cont: int = 0
    for i in nums:
        if i % 2 == 0:
            cont += 1
    return cont


# alternative
def count_even(nums: list[int]) -> int:
    return sum(1 for x in nums if x % 2 == 0)