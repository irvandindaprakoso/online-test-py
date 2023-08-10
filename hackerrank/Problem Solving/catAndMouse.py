def catAndMouse(x, y, z):
    for i in range(q):
        if abs(x-z) < abs(y-z):
            res = 'Cat A'
        elif abs(x-z)> abs(y-z):
            res = 'Cat B'
        elif abs(x-z) == abs(y-z):
            res = 'Mouse C'
    return res
