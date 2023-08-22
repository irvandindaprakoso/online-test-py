def checkMagazine(magazine, note):
    l_m = len(magazine)
    l_n = len(note)
    count = 0
    i = 0
    j = 0
    magazine.sort()
    note.sort()
    while i<l_n and j<l_m:
        if note[i] == magazine[j]:
            count+=1
            i+=1
        j+=1
    if l_n == count:
        print('Yes')
    else:
        print('No')