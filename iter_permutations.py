from itertools import permutations
inpt = 'RAM 3'
str = inpt.split(' ')[0]
str1 = list(str)
n = inpt.split(' ')[1]
arr1 = permutations(str1,int(n))
arr2 = []
for i in arr1:
  arr2.append(''.join(i))

arr2.sort()
for i in arr2:
    print(i)