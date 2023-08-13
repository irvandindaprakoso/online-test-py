def taum_bday(b, w, bc, wc, z):
    # Write your code here
    _x = 0
    _y = 0
    if (bc > wc):
        if (bc-wc > z):
            _x = wc+z
        else:
            _x = bc
    else:
        _x = bc
    
    if (wc > bc):
        if (wc-bc>z):
            _y = bc+z
        else:
            _y = wc
    else:
        _y = wc
        
    res = (b * _x) + (w * _y)

    return res