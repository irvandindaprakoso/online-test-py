def circularArrayRotation(a, k, queries):
    res = []
    if k > n:
        k = k % n
        b = a[-k:]+a[:-k]
        for i,j in enumerate(queries):
            # print (b[j])
            res.append(b[j])
        return res
    else:
        b = a[-k:]+a[:-k]
        for i,j in enumerate(queries):
            # print (b[j])
            res.append(b[j])
        return res
