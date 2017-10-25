# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
str = input()
for i, j in  groupby(str):
    print ((len(list(j)), int(i)), end = ' ')
