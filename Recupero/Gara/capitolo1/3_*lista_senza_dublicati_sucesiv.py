'''
Eco delle Tracce

Gli alambicchi accumulano residui: separa ogni sostanza tenendo solo la prima apparizione.
 Usa `dedup_stable(nums)` per ottenere una nuova lista senza duplicati successivi, 
 mantenendo l'ordine della lista originale. 
Mantieni la firma e supera i test come un filtraggio riuscito.
'''

def dedup_stable(nums: list[int]) -> list[int]:
    nums_2: list[int] = nums.copy()
    nums_3:list[int] = []
    for i in range(len(nums)):
        if i == 0:
            nums_3.append(nums[i])
        elif nums[i] != nums_2[i-1]:
            nums_3.append(nums[i])
    return nums_3

print(dedup_stable([1,3,1,4,2,3,1]))


print(dedup_stable([1,1,2,2,3,3]))

# alternative

def dedup_stable(nums: list[int]) -> list[int]:
    out: list[int] = []
    prev = object()          # valore impossibile da eguagliare
    for x in nums:
        if x != prev:
            out.append(x)
            prev = x
    return out

def dedup_stable(nums: list[int]) -> list[int]:
    out: list[int] = []
    for x in nums:
        if not out or x != out[-1]:
            out.append(x)
    return out
