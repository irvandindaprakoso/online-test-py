def staircase(n):
    i = 1
    j = n-1
    while i<n+1:
        print(' '*j+'#'*i)
        i+=1
        j-=1
