a=[4,2,5,10,6,12,7,1,-3]
key=5
ans=False
for i in range(len(a)):
    if(a[i]==key):
       ans=i
       break
if ans==False:
    print("not found")
else:
    print("found",ans)