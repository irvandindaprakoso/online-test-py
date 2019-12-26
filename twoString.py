def TwoString(s1,s2):
    l_s2 = sorted(list(s2))
    l_s1 = sorted(list(s1))
    for i in l_s1:
        if i not in l_s2:
            print('YES')
            break
    else:
        print('NO')
s1 = input()
s2 = input()
print(TwoString(s1,s2))