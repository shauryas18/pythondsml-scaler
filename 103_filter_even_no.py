# l = [21,24,27,46,48,6,25,38,10,40]

for i in l:
    if i % 2 == 0:
        print(i)

# # other method
a=[21,24,27,46,48,6,25,38,10,40]
b=[]
for i in a:
   if i % 2 == 0:
       b.append(i)

# list comprehension
a=[21,24,27,46,48,6,25,38,10,40]
b=[x for x in a if x%2==0]
print(b)