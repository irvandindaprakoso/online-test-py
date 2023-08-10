def migratoryBirds(arr):
    max_c = [0]*6

    for i, v in enumerate(arr):
        max_c[arr[i]]+=1
    return max_c.index(max(max_c))
