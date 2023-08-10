def plusMinus(arr):
    plus =0 ; minus = 0; zero = 0;
    for i in range(n):
        if arr[i] >0:
            plus +=1
        elif arr[i]<0:
            minus+=1
        else:
            zero+=1
        res_p = plus/n
        res_m = minus/n
        res_z = zero/n
    print(res_p)
    print(res_m)
    print(res_z)
