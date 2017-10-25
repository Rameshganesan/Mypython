# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
arr = input().split(' ')
s = set(arr)
N1 = input()
for i in range(0,int(N1)):
   inpt = input()
   print(inpt)
   in1 = inpt.split(' ')[0]
   if in1 == 'pop':
      try:
         s.pop()
      except KeyError:
         pass
   elif in1 == 'remove':
      try:
         s.remove(inpt.split(' ')[1])
      except KeyError:
         pass
   elif in1 == 'discard':
      s.discard(inpt.split(' ')[1])
for i in s:
   print(i)