def pickingNumbers(a):
    # Write your code here
    max = 0
    for i in a:
        c = a.count(i)
        d = a.count(i-1)
        e = c+d
        if e>max:
            max = e
    return max
