# #Find Logarithm
import math

num = float(input("Enter a number: "))
print("Natural log (ln):", math.log(num))
print("Log base 10:", math.log10(num))


#Trigonometric Functions
import math

angle = float(input("Enter angle in degrees: "))

# convert to radians
rad = math.radians(angle)

print("Sin:", math.sin(rad))
print("Cos:", math.cos(rad))
print("Tan:", math.tan(rad))


# #Find LCM using math
import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm = abs(a*b) // math.gcd(a, b)
print("LCM is:", lcm)


# #Check Prime Number (using sqrt)
import math

num = int(input("Enter number: "))

if num < 2:
    print("Not Prime")
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")