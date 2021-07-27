def pageCount(n, p):
    #
    # Write your code here.
    #
    total = n//2
    right = p//2
    left = total - right
    if right> left:
        return left
    else:
        return right
