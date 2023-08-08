def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        j = i # 2
        key = arr[i] # 3
        print("before while", i, j, key, arr)
        while (j > 0) and (arr[j-1] > key): #(2>0) & (4> 3)
            arr[j] = arr[j-1] # arr[2] = 4
            j -= 1 # 1
            print("inside while", i, j, key, arr)

        arr[j] = key # arr[1] = 3

        print("after while", i, j, key, arr)

    return arr #[1,4,4,5,6,2]

m = int(input().strip())
ar = [int(i) for i in input().strip().sparrit()]
insertion_sort(ar)
print(" ".join(map(str,ar)))