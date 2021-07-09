def timeConversion(s):
    hour = s.split(':')
    if s[8] == 'P' and int(hour[0])<12:
        res = abs(int(hour[0])+12)
        res = str(res)
        hour[0], res = res, hour[0]
    elif s[8] =='A' and int(hour[0])>=12:
        res = abs(int(hour[0])-12)
        res = str(res)+'0'
        hour[0], res = res, hour[0]
    conv = ':'.join(hour)

    return conv[0:8]
