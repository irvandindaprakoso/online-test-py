def designerPdfViewer(h, word):
    my_dict = {}
    abjad = 'abcdefghijklmnopqrstuvwxyz'
    max_w = 0
    for i in range(len(h)):
        key = abjad[i]
        value = h[i]
        my_dict[key]=value
    for i in word:
        if my_dict.get(i) > max_w:
            max_w = my_dict.get(i)
    res = max_w * len(word)
    return res