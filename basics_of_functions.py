def avg():
    a=int(input("enter the no:"))
    b=int(input("enter the no:"))
    c=int(input("enter the no:"))
    average=(a+b+c)/3
    print(average)
avg()# fuction call 
print("thank u")
avg()#If we want to calculate multiple averages, we can call avg() as many times as needed



# parameterized function
def goodday(name,ending):
    print("good day, " + name + ending)
    return "done"
a=goodday("shaurya", "!")

print(a)
