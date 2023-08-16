def minimumDistances(a):
    res = []
    reverse= -1
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if (a[i]==a[j]):
                hasil = abs(i-j)
                res.append(hasil)
    if res:
        return min(res)
    else:
        return reverse