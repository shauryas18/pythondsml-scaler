def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


# Taking input
num = int(input("Enter a number: "))

# Function call
result = factorial(num)

# Output
print("Factorial is:", result)