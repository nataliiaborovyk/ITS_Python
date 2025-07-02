'''

Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.

For example:
Test 	Result

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))


{'Alice': [90, 85], 'Bob': [75]}     print(aggrega_voti([])) 

'''
diz = ([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}])

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    diz_nuovo:dict = {}
    for i in voti:
        if i["nome"] in diz_nuovo:
            diz_nuovo[i["nome"]].append(i["voto"])
        else:
            diz_nuovo[i['nome']] = [i['voto']]

    return diz_nuovo
            

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))


# def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
#     diz_nuovo:dict = {}
#     for i in voti:
#         k = i[1]
#             if v in diz_nuovo:
#                 diz_nuovo[0].append()
#             else:
#                 diz_nuovo[k] = [v]
#     return diz_nuovo

# print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
