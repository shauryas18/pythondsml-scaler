#simple fuction with an argument
def hello(name):
    print("hello " + name)
hello("john")


#additon of no using fuction
def add(a, b):
   # print (a + b)
    print("a+b =", (a + b))

a=int(input("enter the no a: ") )
b=int(input("enter the no b: ") )
add(a, b)

# pass multiple argument in fuction
def fight(name,states,age="30" ):
    print("name",name,"age",age,"state",states)
fight("john", "delhi", 25)#if no age provide it take by default 30

#returning data from a function
def cube(x):
    ans=x**3
    return ans
print(cube(3))
