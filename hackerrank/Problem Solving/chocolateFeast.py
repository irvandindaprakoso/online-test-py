def chocolate_feast(n, c, m):
    
    choco = n//c
    res = 0
    if choco==m:
        res = choco +1
    elif choco<m:
        res = choco
    else:
        res = choco
        while choco >= m:
            choco -= m 
            choco += 1 
            res +=1
    return res