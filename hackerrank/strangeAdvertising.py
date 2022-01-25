def viralAdvertising(n):
    shared = 5
    list_like = []
    for i in range(n):
        like = shared//2
        shared = like * 3
        list_like.append(like)
    return sum(list_like)
