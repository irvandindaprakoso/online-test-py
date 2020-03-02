N = input().split()
arr = list(map(int, input().split()))
result = []
res = 0

for i in range(int(N[1])):
    inp = list(map(int,input().split()))
    q,w,e = inp[0], inp[1], inp[2]
    if q == 1:
        arr[w] = e
    elif q > 1:

        for x in range(w,e+1):
            res += arr[x]
        result.append(res)
        res = 0

for i in result:
    print(i)
