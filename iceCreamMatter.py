inputan = input().split()
late = int(inputan[0])
increment = int(inputan[1])
res = 0

if late < 11:
    for i in range(1,late+1):
        res += (increment*i)
    print(res)
else:
    print('Invalid input')

