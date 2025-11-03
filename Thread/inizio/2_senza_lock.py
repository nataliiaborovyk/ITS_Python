import threading, time

x = 0

def incrementa():
    global x
    for _ in range(100000):
        temp = x
        time.sleep(0.000001)  # 👈 pausa minuscola per aumentare collisioni
        x = temp + 1

t1 = threading.Thread(target=incrementa)
t2 = threading.Thread(target=incrementa)

t1.start(); t2.start()
t1.join(); t2.join()

print(f"x finale = {x}")
