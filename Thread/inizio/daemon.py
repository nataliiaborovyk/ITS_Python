import time, threading

def ticker():
    while True:
        print("[daemon] tic")
        time.sleep(0.5)

d = threading.Thread(target=ticker, name="Ticker", daemon=True)  # daemon=True
d.start()

print("Faccio una cosa veloce nel main...")
time.sleep(1.2)
print("Fine del main: il daemon verrà chiuso automaticamente.")
