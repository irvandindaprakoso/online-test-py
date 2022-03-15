
def reversedInt(num: int) -> int:
    result = 0
    while num:
        lastDigit = num % 10
        result = result * 10 + lastDigit
        if result < -2 ** 31 or result > 2 ** 31:
            return 0
        num //=10
    return result

print(reversedInt(1534236469))
print(reversedInt(2147483641))