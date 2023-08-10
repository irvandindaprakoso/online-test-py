def kangaroo(x1, v1, x2, v2):    
    res1=x1; res2=x2
    if x1<x2 and v1<v2:
        return 'NO'
    else:
        for i in range(10000):
            res1 += v1
            res2 += v2
            if res1 == res2:
                return 'YES'
                break
        else:
            return 'NO'
