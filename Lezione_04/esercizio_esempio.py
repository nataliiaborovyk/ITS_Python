
sum1:int = 0
for i in range(1, 11):
    sum1 += i
print(sum1)

sum2:int = 0
for i in range(20,38):
    sum2 += i
print(sum2)

sum3:int = 0
for i in range(35,50):
    sum3 += i
print(sum3)

def subtract(a:int, b:int):
    if a > b:
        subtract:int = a -b
    else:
        subtract:int = b -a
    return subtract

print(f"La sottrazione: {subtract(5,8)}")


def subtract_2(a:int, b:int):
    subtract = a - b
    print(f"a: {a}\nb: {b}")
    return subtract

print(f"il risultato è {subtract_2(2,8)} di sottrazione tra a e b")
print(type(subtract_2(2, 7)))


def subtract_2(a:int, b:int) -> int:
    subtract:int = a - b
    print(f"a: {a}\nb: {b}")
    return subtract

#print(f"Il risultato di sottrazione è: {subtract_2(int(input("inserisci a: ")), int(input("inserisci b: ")))}")

print(subtract_2(int(input("inserisci a: ")), int(input("inserisci b: "))))



def operations(a:int, b:int) -> tuple[int, int]:
    sum_result:int = a + b
    diff_risult:int = a - b
    print(f"a: {a}\nb: {b}")
    return sum_result, diff_risult

sum_value, diff_value = operations(10, 5)
print("Sum: ", sum_value)
print("Difference: ",diff_value)
print(type(operations(10, 5)))

def get() -> list[float]:
    return [12.5, 45.8]

coords = get()
print(coords[0], coords[1], sep=", ")



