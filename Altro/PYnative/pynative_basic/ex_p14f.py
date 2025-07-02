'''
Exercise 14: Print a downward half-pyramid pattern of stars
'''

x:int =int(input("Inserisci il numero: "))

for i in range(x,0,-1):
    for k in range(i,0,-1):
        print("*", end=" ")
    print("")
        

