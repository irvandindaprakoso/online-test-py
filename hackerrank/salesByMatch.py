def sockMerchant(n, ar):
    set_arr = set(ar)
    res = 0
    for i in set_arr:
        x = ar.count(i)
        x = x//2
        res+=x
    return res
