# file = open("exemple.txt", "a")
# print(file) 

# file.close()
#altra vesrsione

with open("exemple.txt", "r") as file:
    # stringa: str ="Ciao"
    # file.write(stringa)
    print(file.read())

    