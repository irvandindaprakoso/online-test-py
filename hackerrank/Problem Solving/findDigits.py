def findDigits(n):
    count = 0
    for i in str(n):
        if i != '0':
            res = n % int(i)
            if res == 0:
                count +=1
    return count