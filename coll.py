from collections import Counter

a = 'Today is is ddd Today'
b = a.split(' ')
print(b)
counts = Counter(b)
print(counts)
for i in b:
    va = counts.pop(i, None)
    if va == None:
        continue
    else:
        print(va,)






