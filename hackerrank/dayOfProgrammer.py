def dayOfProgrammer(year):
    list_day = [31,28,31,30,31,30,31,31]
    if year == 1918:
        day = 26
    elif ((year < 1918) & (year%4 == 0)) or ((year%400 == 0) or ((year%4 ==0) & (year%100 != 0))):
        day = abs(sum(list_day)+1-256)
    else:
        day = abs(sum(list_day)-256)
    return str(day)+'.09.'+str(year)
