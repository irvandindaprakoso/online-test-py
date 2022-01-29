def saveThePrisoner(n, m, s):
    res = (m+s-1)%n
    if res==0:
        return n
    else:
        return res
