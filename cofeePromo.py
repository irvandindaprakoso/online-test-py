cup = int(input())
arr = []
L = 20000
C = 25000
A = 20000
W = 5000
for i in range(cup):
    arr.append(input().upper())

res = 0
flag = 0
for i in arr:
    if i == 'L':
        res+= L
        if flag <=2:
            flag = 2
    elif i== 'C':
        res+= C
        if flag <= 3:
            flag = 3
    elif i =='A':
        res+=A
        if flag <=2:
            flag = 2
    else:
        res+=W
        if flag <=1:
            flag = 1
    
if flag == 1:
    res-=2000
elif flag ==2:
    res-=17000
else:
    res-=22000

print(res)