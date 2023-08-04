def repeatedString(s, n):
    res= s.count("a")*(n // len(s)) + s[:n % len(s)].count("a")
    return res