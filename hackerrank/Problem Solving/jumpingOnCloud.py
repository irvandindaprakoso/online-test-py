def jumping_on_clouds(c):
    count = 0
    i=0
    while i < len(c)-1:
        if(i+2<len(c) and c[i+2]==0):
            count+=1
            i=i+2
        else:
            count+=1
            i+=1
    return count