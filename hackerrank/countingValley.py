def countingValleys(n, s):
    v=0
    result=0
    for n in s:
        if (n=="U"):
            v+=1
        elif(n=="D"):
            v-=1
        
        if(v==0 and n=="U"):
            result+=1
    return result
