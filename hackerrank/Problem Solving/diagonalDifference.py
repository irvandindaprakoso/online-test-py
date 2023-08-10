# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        sum1 += arr[i][i]
        sum2 += arr[i][n-1-i]
        res = sum1-sum2
    return abs(res)
