# Complete the utopianTree function below.
def utopianTree(n):
    res = 1
    if n != 0:
        for i in range(n):
            if i % 2 == 0 :
                res = res * 2
            else:
                res +=1
        return res
    else:
        return res
