# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

st1 = 'This is the day'
str, n = st1.split(' '),3
arr2 = []
for i in range(1,int(n)+1):
    for j in combinations(sorted(str),i):
        arr2.append(j)
#arr2.sort(key=lambda list:list[0])
for i in arr2:
    print(''.join(i))