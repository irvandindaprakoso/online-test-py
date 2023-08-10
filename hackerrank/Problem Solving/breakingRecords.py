def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    count_max = 0
    count_min = 0
    for i in scores:
        if i > max_score:
            max_score = i
            count_max +=1
        elif i < min_score:
            min_score = i
            count_min +=1
    return count_max, count_min
