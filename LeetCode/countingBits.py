def countingBits(n):
    result = []
    for i in range(n+1):
        count = 0
        biner = bin(i).replace("0b","")
        for val in biner:
            if val == '1':
                count+=1
        result.append(count)
    return result

print(countingBits(5))
