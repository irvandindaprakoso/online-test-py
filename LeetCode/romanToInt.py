def romanToInt(s):
    roman_val = {'I' : 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    int_val = 0
    for i in range(len(s)):
        print(s, i, s[i], roman_val[s[i]], roman_val[s[i - 1]])
        if i > 0 and roman_val[s[i]] > roman_val[s[i - 1]]:
            int_val += roman_val[s[i]] - 2 * roman_val[s[i - 1]]
            print(roman_val[s[i]], 2 * roman_val[s[i - 1]])

        else:
            int_val += roman_val[s[i]]
            print (roman_val[s[i]])
    return int_val

print(romanToInt('MCMXCIV'))