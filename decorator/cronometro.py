def cronometro(fun):
    def wrapper():
        import time
        start = time.time()
        fun()
        print(time.time() - start)
    return wrapper

@cronometro       #   prova = cronometro(prova)
def prova():
    for i in range(1000000):
        pass

prova()

def cronometro1(fun):
    def wrapper(*args):
        import time
        start = time.time()
        fun(*args)
        print(time.time() - start)
    return wrapper

@cronometro1       #   prova = cronometro(prova)
def prova1(n):
    for i in range(n):
        pass

prova1(5000000000)