firstlst: list[int] = [1, 2, 3, 4, 5]
firstlst.extend( {8, 7, 6} )
print(firstlst[5])
print(type(firstlst[5]))

firstlst: list[int] = [1, 5, 7, 8] 
secondlst: list[int] = [2, 3, 7, 6]
hirdlst: list[int] = firstlst + secondlst
print(hirdlst)
