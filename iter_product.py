# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = map(int, input().strip('\r').split(' '))
b = map(int, input().strip('\r').split(' '))
x = ''
c = list(product(a,b))
for i in c:
  x = x + str(i) + ' '
print(x)
