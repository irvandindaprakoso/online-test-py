def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    max_c = 0
    list_things =[]
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            res = keyboards[i]+ drives[j]
            if res <=b:
                list_things.append(res)
    if len(list_things)==0:
        return '-1'
    else:
        return max(list_things)
