T = int(input())

def taumBday(b,w,bc,wc,z):
    _b = 0
    _w = 0
    if (bc > wc):
        if (bc-wc > z):
            _b = wc + z
        else:
            _b = bc
    else:
        _b = bc
    
    if (wc > bc):
        if (wc - bc> z):
            _w = bc+z
        else:
            _w = wc
    else:
        _w = wc
    
    res = (b * _b) + (w * _w)

    return res


for i in range(T):
    arr_input = input().split()
    b = int(arr_input[0])
    w = int(arr_input[1])
    arr_input2 = input().split()
    bc = int(arr_input2[0])
    wc = int(arr_input2[1])
    z = int(arr_input2[2])
    print(taumBday(b,w,bc,wc,z))

