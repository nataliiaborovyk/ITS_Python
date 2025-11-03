'''
Censimento delle Essenze

Nel giardino delle essenze annoti quante specie davvero distinte sono state raccolte. 
Usa `unique_count(nums)` per restituire il conteggio degli interi unici in `nums`. 
Mantieni la firma e lascia che i test profumino di rigore.
'''

def unique_count(nums: list[int]) -> int:
    diz: dict = {}
    for i in nums:
        if i in diz:
            diz[i] += 1
        else:
            diz[i] = 1
    return len(diz)


# alternative

def unique_count(nums: list[int]) -> int:
    return len(set(nums))


def unique_count(nums: list[int]) -> int:
    seen: set[int] = set()
    for x in nums:
        seen.add(x)
    return len(seen)



from collections import Counter

def unique_count(nums: list[int]) -> int:
    return len(Counter(nums))


def unique_count(nums: list[int]) -> int:
    if not nums:
        return 0
    s = sorted(nums)   # non tocchi la lista originale
    count = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            count += 1
    return count

