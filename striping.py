#  remove data from list


def rem(l, word):
    for i in l:
        l.remove(word)
        return l
l=['hello', 'world', 'hello', 'python','o']
print(rem(l, 'o'))




# strip data from list
def rem(l, word):
   n=[]
   for i in l:
       if i != word:
              n.append(i.strip(word))
   return n

l=['hello', 'world', 'hello', 'python','o']
print(rem(l, 'o'))


