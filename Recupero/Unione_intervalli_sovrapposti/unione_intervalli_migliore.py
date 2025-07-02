
def merge_intervals(intervals) -> list[list[int]]:

    if len(intervals) <= 1:
       return intervals      #qui finisce programma

    intervals.sort(key=lambda x: x[0])

    nuova_lista: list[list[int]] = [intervals[0]]

    for succesivo_intervallo in intervals[1:]:
        ultimo_intervallo = nuova_lista[-1]   
        if succesivo_intervallo[0] <= ultimo_intervallo[1]:
            ultimo_intervallo[1] = max(ultimo_intervallo[1], succesivo_intervallo[1])
        else:
            nuova_lista.append(succesivo_intervallo)            
    
    return nuova_lista




if __name__ == "__main__":
    intervals1 = [[1, 3], 
                 [2, 6], 
                 [8, 10], 
                 [15, 18]
                 ]
    intervals2 = [[1, 4]]
    intervals3 = [[1, 4], [4, 5], [4,8]]
    intervals4 = []

    '''
    i=0 k=1
    i=1 k=0

    i=1 k=1
    i=2 k=0

    i=2 k=1
    i=3 k=0

    '''
    print(merge_intervals(intervals1))
    print(merge_intervals(intervals2))
    print(merge_intervals(intervals3))
    print(merge_intervals(intervals4))