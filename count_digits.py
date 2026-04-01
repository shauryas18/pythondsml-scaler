# Program to count the total number of digits in a number

number = int(input("Enter a number: "))
count = 0

number = abs(number)

# If the number is 0, it has 1 digit
if number == 0:
    count = 1
else:
    while number > 0:
        number //= 10 
        count += 1

print("Total number of digits:", count)