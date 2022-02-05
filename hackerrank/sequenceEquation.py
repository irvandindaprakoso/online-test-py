def permutationEquation(p):
    tes = []
    for i in range(1,n+1):
        count = 1
        res = 1
        for j in range(n):
            if i == p[j]:
                break
            count +=1
        for k in range(n):
            if count == p[k]:
                break
            res +=1
        tes.append(res)
    return tes
