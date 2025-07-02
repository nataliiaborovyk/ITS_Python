'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides,
 and it should print a summary of the sandwich that’s being ordered. Call the function three times,
   using a different number of arguments each time.
'''

print("\n   Esercizio 8-12")


# VERSIONE 1
print("\n Versione 1")

def sandwich(*args, x = "pane"):

    print(f"\nIl tuo sandwich contiene: ")

    for i in args:
        print(i)

    print(x)
    
sandwich("pomodoro", "rucola", "salame")
sandwich("pomodoro", "rucola", "salame", x = "pane integrale")
sandwich("tonno", "pomodoro")


# VERSIONE 2
print("\n Versione 2")

def sandwich(*args, x = "pane"):
    print(f"\nIl tuo sandwich contiene: ")
    print(*args, x)

sandwich("pomodoro", "rucola", "salame")
sandwich("pomodoro", "rucola", "salame", x = "pane integrale")
sandwich("tonno", "pomodoro")



# VERSIONE 3
print("\n Versione 3")

def sandwich(*args, x = "pane"):

    lista: lista = [x]

    print(f"\nIl tuo sandwich contiene: ")

    for i in args:
        lista.append(i)

    print(*lista, sep=", ")
    #print(x, *args, sep=", ")

sandwich("pomodoro", "rucola", "salame")
sandwich("pomodoro", "rucola", "salame", x = "pane integrale")
sandwich("tonno", "pomodoro")


