def hurdleRace(k, height):
    max_h = max(height)
    if max_h > k:
        res = max_h - k
    else:
        res = 0
    return res
