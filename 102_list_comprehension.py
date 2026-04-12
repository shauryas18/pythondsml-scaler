# generate a list of square of all number between 1 to 100

# using for loop
square=[]
for i in range(1,101):
    square.append(i**2)
print(square)

# using list comprehension
square2=[i**2 for i in range(1,101)]
print(square2)

#using map fuction
def squ(x):
    return x**2
result=list(map(squ,range(1,101)))
print(result)