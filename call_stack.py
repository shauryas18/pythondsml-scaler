m=100   #local variable (we can read anywhere in the program)
y=10
def square(x):
   print("m=",m)
   y=5             #inside function it declared as a local variable
   print("y=",y)
   return x**2
def pythagoras(a,b):
     c2=square(a)+square(b)
     return c2
c3=pythagoras(4,5)
print(c3)
print("y=",y)       #output 10 because y is a global variable and we can read it anywhere in the program



#global function is used to declare a variable as global inside a function
m=100   #local variable (we can read anywhere in the program)
y=10
def square(x):
   print("m=",m)
   global y
   y=5             #inside function it declared as a local variable
   print("y=",y)
   return x**2
def pythagoras(a,b):
     c2=square(a)+square(b)
     return c2
c3=pythagoras(4,5)
print(c3)
print("y=",y)       #output 5 because y is declared as global and its value is modified inside the function