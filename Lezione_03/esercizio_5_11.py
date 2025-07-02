'''
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, 
such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal 
ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", 
and each result should be on a separate line.
'''

#esercizio 5-10
print("\n Esercizio 5-10 \n")

lista: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in lista:
    if i == 1:
        print(f"{i}st")
    elif i == 2 or i == 3:
        print(f"{i}nd")
    elif i >= 4 or i <= 9:
        print(f"{i}th")