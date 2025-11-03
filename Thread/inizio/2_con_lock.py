import threading, time

x = 0
lock = threading.Lock()

def incrementa():
    global x
    for _ in range(100000):
        time.sleep(0.000001) # deve stari fuori lock, altrimenti aumenta il tempo di esecuzione
        with lock:
            x += 1

t1 = threading.Thread(target=incrementa)
t2 = threading.Thread(target=incrementa)

t1.start(); t2.start()
t1.join(); t2.join()

print(f"x finale = {x}")
