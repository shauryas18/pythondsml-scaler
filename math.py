#log function
import math
print(math.log(1))
print(math.log(125,5))
print(math.log2(8))

# GCD function (only for two value)
a=int(input("enter the no:" ))
b=int(input("enter the no:"))
while a!=0:
    a,b=a%b,a
    print("gcd is:",b)


# GCD for multuple value
a=int(input("enter the no:" ))
b=int(input("enter the no:"))
def gcd(a,b):
 while a!=0:
    a,b=a%b,a
 return b
print("gcd is:",gcd(a,b))
import math

import math

nums = list(map(int, input("Enter numbers: ").replace(',', ' ').split()))
print("GCD is:", math.gcd(*nums))