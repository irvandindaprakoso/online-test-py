hour = int(input())
res = 0
for i in range(1,hour+1):
    res+= 4000
    if i%5==0:
        res-=2000
print(res)