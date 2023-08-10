def how_many_games(p, d, m, s) :
    result = 0
    current_price = p
    while s >= current_price:
        s-= current_price
        result+=1
        current_price = max(current_price - d, m)
    return result


print(how_many_games(20, 3, 6, 80))