def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i):
            res = ar[i]+ar[j]
            if res==k:
                count+=1
            elif res % k == 0:
                count+=1
    return count
