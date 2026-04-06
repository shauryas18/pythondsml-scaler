for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()

    #output
#     * 
#     * * 
#     * * * 
#     * * * * 

# OR
n=int(input("input the number:"))
for i  in range(1,n+1):
   print("*"*i, end="") 
   print("")