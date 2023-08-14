def beautiful_triplets(d, arr):

    res = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (abs(arr[i]-arr[j])==d):
                for k in range(j, len(arr)):
                    if (abs(arr[j]-arr[k])==d):
                        res+=1
                        break
                break
    return res