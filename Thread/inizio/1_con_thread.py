# file: con_thread.py
import time
import threading  # modulo per i thread

def lavoro(nome, secondi):
    # threading.current_thread().name restituisce il nome del thread che sta eseguendo ora
    print(f"[{nome}] start su thread: {threading.current_thread().name}")
                                    # threading.current_thread().name: dà il nome del thread corrente (per debug/log).
    
    time.sleep(secondi)  # simula I/O

    print(f"[{nome}] end   su thread: {threading.current_thread().name}")



t0 = time.perf_counter()

# Creiamo 2 thread che eseguono la stessa funzione con parametri diversi
t1 = threading.Thread(target=lavoro, args=("download_1", 2), name="T-1") # threading.Thread(...): classe che rappresenta un thread.
                    # target=...: la funzione che il thread dovrà eseguire.
                                 # args=(...): tuple con gli argomenti da passare a target.
                                            # name="T-1": nome del thread (utile per capire chi sta stampando).
t2 = threading.Thread(target=lavoro, args=("download_2", 2), name="T-2")

t3 = threading.Thread(target=lavoro, args=("download_3", 2), name= "T-3 Nat")

# Avvio: parte davvero in parallelo (concorrenza)
t1.start()   # .start(): avvia il thread (inizia a eseguire target in parallelo).
t2.start()
t3.start()

# join() = aspetta che quel thread finisca
# t1.join()   # .join(): il programma principale aspetta quel thread (sincronizzazione).
# t2.join()
# t3.join()

        # t1_fine = not t1.is_alive()  # False se ancora vivo, True se 
        #                 # .is_alive(): dice se il thread è ancora in esecuzione.
        # t2_fine = not t2.is_alive()

t1 = time.perf_counter()  # time.perf_counter(): cronometro preciso per misurare la durata.
        # print(f"t1 finito? {t1_fine} | t2 finito? {t2_fine}")
print(f"Tempo totale (con thread): {t1 - t0:.2f}s")
