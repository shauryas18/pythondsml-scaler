# s is a binary string
def binaryToDecimal(s):
    i = 0
    result = 0

    for digit in s[::-1]:
        result += int(digit) * (2 ** i)
        i = i + 1

    return result


# Example
print(binaryToDecimal("10100"))  # Output: 20