from collections import Counter
a = 'This world is small but it is vast'
b = a.split(' ')
c = Counter(b)
print(c)
for i in c.items():
   print(i[0]+' --> '+str(i[1]))



