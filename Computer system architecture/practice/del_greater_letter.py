def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1 
# Driver code 
str1=input()
l = Convert(str1)
k = list(l.count(i) for i in l)
i = 0
val = k.count(max(k))
while (i < val):
    l.remove(l[k.index(max(k))])
    k.remove(max(k))
    i = i+1

print(''.join(l))