# file: senza_thread.py
import time  # modulo per dormire (simulare I/O)

def lavoro(nome, secondi):
    print(f"[{nome}] inizio")
    time.sleep(secondi)  # simula attesa I/O (es. rete/disk)
    print(f"[{nome}] fine")

t0 = time.perf_counter()     # orologio ad alta precisione
lavoro("download_1", 2)      # fa tutto il primo
lavoro("download_2", 2)      # poi il secondo (solo dopo il primo)
t1 = time.perf_counter()

print(f"Tempo totale (sequenziale): {t1 - t0:.2f}s")




def cronometro(fun):
    def wrapper(*args):
        import time
        start = time.time()
        fun(*args)
        tempo = time.time() - start
        print(f"Tempo impiegato: {tempo:.2f}s")
    return wrapper
    
@cronometro
def lavoro_decorato(nome:str, secondi:float):
    print(f"{nome}: inizio")
    time.sleep(secondi)
    print(f"{nome}: fine")

print()

lavoro_decorato("download1", 2)

print()

lavoro_decorato("download2", 3)