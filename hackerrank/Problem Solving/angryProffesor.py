def angryProfessor(k, a):
    count = 0
    for i, j in enumerate(a):
        if j <=0:
            count+=1
    if count >= k:
        return 'NO'
    else:
        return 'YES'
