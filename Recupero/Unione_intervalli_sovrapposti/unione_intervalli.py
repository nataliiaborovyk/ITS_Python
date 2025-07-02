
def merge_intervals(intervals) -> list[list[int]]:
    
    intervals.sort(key=lambda n: n[0])
    
    nuova_lista: list[list[int]] = []

    for i in range(len(intervals)):
        for k in range(len(intervals[i])):
            if k == 1:
                num_end = intervals[i][k]
            elif k == 0 and i != 0:
                num_start = intervals[i][k]
                if num_end >= num_start:
                    nuova_lista.append([intervals[i-1][0], intervals[i][k+1]])
                else:
                    nuova_lista.append([intervals[i][0], intervals[i][k+1]])
            
    
    return nuova_lista


if __name__ == "__main__":
    intervals1 = [[1, 3], 
                 [15, 18],
                 [2, 6], 
                 [8, 10]
                 ]
    intervals2 = [[1, 4], [4, 5]]
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