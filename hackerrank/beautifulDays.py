def beautifulDays(i, j, k):
    count =0
    for a in range(i, j+1):
        day = str(a)
        rev_day = int(day[::-1])
        res = (abs(a - rev_day) % k)
        if res == 0:
            count +=1
        # print(a, day, rev_day,res, count)
    return count
