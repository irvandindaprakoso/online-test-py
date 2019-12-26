arr = [int(x) for x in input().split()]
max_c = [0]*6
for i, v in enumerate(arr):
    max_c[arr[i]]+=1
    print(max_c)
print (max_c.index(max(max_c)))