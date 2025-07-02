#Exercise 2: Print the following pattern

#Write a Python code to print the following number pattern using a loop.

len:int = int(input("Write the size of pattern: "))

for i in range(len+1):
    for k in range(i):
        print(i, end=" ")
    print("")

for i in range(len+1):
    for k in range(1, i+1):
        print(k, end=" ")
    print("")