def countApplesAndOranges(s, t, a, b, apples, oranges):
    a = [a]
    b = [b]
    count_apples =0
    count_oranges = 0
    adding_apples = [sum(i) for i in zip(apples, a*m)]
    adding_oranges = [sum(i) for i in zip(oranges, b*n)]
    # print(adding_apples, adding_oranges)
    for i in adding_apples:
        if i >= s and i<=t:
            count_apples += 1
    for i in adding_oranges:
        if i >=s and i<=t:
            count_oranges+=1
    print (count_apples)
    print(count_oranges)
