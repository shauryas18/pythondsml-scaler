n=int(input("Enter the number: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"* n, end="")
        print("")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
        print("")


        #output
#Enter the number: 5
# *****
# *   *
# *   *
# *   *
# *****