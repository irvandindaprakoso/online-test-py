def birthdayCakeCandles(ar):
    count = 0
    max_ar = max(ar)
    for i in range(len(ar)):
        if ar[i] == max_ar:
            count+=1
    return count
