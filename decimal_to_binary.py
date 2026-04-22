# def decimalToBinary(n):
#     return bin(n)[2:]


# print(decimalToBinary(20))  # Output: 10100



def decimalToBinary(n):
    l = []
    while n > 0:
        remainder = n % 2
        l.append(remainder)
        n = n // 2

    # Reverse the list
    l = list(reversed(l))
    return l


# Example
print(decimalToBinary(20))   # Output: [1, 0, 1, 0, 0]