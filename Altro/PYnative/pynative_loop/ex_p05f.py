#Exercise 5: Display numbers from a list using a loop

lista:list = [12, 75, 150, 180, 145, 525, 50]

for i in lista:
    #if i > 500:
        #break
        if i >= 150:
            continue
        elif i % 5 == 0:
            print(i)
        elif i > 500:
            break
