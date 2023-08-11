def equalizeArray(arr):
    max_list = 0
    res = [j for i,j in enumerate(arr,1) if j not in arr[i:]]
    for i in res:
        if arr.count(i) > max_list:
            max_list = arr.count(i)
    tes = len(arr) - max_list
    return tes