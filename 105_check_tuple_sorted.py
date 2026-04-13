# #check tuple are sorted or not
 
a=(2,3,5,6,9,11)
ans="sorted"
for i in range(len(a)-1):
    if(a[i]<=a[i+1]):
       continue
       
    else:
        ans="not sorted"
        break
print(ans)
#output:sorted

b=(2,3,5,6,9,2)
ans="sorted"
for i in range(len(b)-1):
    if(b[i]<=b[i+1]):
       continue
       
    else:
        ans="not sorted"
        break
print(ans)
#output:not sorted