def miniMaxSum(arr):
    arr.sort()
    sum1 = sum(arr[0:len(arr)-1])
    sum2 = sum(arr[1:len(arr)])
    print(sum1, sum2)
