def baricentro(v: list[int]):
    sum1 = 0
    sum2 = 0
    for i in range(len(v)):
        for k in range(i+1):
            sum1 += v[k]
        n = i+1
        for j in range(n, len(v)):
            sum2 += v[j]
        if sum1 == sum2:
            return i
        sum1 = 0
        sum2 = 0
        
    return None

v = [1,2,3,3,2,1]
print(baricentro(v))

def baricentro2(v: list[int]):  #sbagliato
    sum1 = 0
    sum2 = 0
    indice = 0
    for i in range(len(v)):
        sum1 += v[i]
        if v[i] == sum1:
            indice = i
    for k in range(indice+1, len(v)):
        sum2 += v[k]
    if v[indice] == sum2:
        return v[indice]
    
print(baricentro2(v))

def baricentro3(v: list[int]):
    for i in range(len(v)):
        sum1 = sum(v[: i+1])
        sum2 = sum(v[i+1 :])
        if sum1 == sum2:
            return i
    return None
print(baricentro3(v))


    
