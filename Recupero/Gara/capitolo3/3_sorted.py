'''
Cristalli Condivisi

Due ricettari mostrano reagenti condivisi. Distillali con `intersection_sorted(a, b)`, 
restituendo una lista ordinata degli interi presenti in entrambi, senza ripetizioni. 
Mantieni la firma e titola i test alla perfezione.
'''

def intersection_sorted(a: list[int], b: list[int]) -> list[int]:
    s1: set[int] = set(a)
    s2: set[int] = set(b)
    s3: set[int] = s1 & s2
    c :list = list(s3)
    c1 : list = sorted(c)
    return c1


a=[1,2,2,3]
b=[2,2,4]
print(intersection_sorted(a,b))

# alternative

def intersection_sorted(a: list[int], b: list[int]) -> list[int]:
    return sorted(set(a) & set(b))
