#bobble sort
a=[2,4,9,6,4,1]
n=len(a)
for i in range (n):
    for j in range(0,n-1):#move 0 to 4 index
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
print(a)