
def alphabet_rangoli(size) :
    alphabet = [chr(i) for i in range(97, 123)][:size]
    indices = list(range(size))
    indices = indices[:-1] + indices[::-1]
    
    for i in indices:
        start_index = i + 1
        original = alphabet[-start_index:]
        reverse = original[::-1]
        row = reverse + original[1:]
        row = "-".join(row)
        width = size * 4 - 3
        row = row.center(width, "-")
        print(row)

size= 3
print(alphabet_rangoli(size))