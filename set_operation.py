# find the symmetric difference from set - uncommon value from the set.
# a = int(input())
# a1 = map(int,input().split())
# b = int(input())
# b1 = map(int, input().split())
# s1 = set(a1)
# s2 = set(b1)
# s3 = set(s1.symmetric_difference(s2))
# for i in sorted(s3):
#     print(i),

# Adding string to the set
s = set("HacketRank")
print(s)
print(s.add('HackerRank'))
print(s)

# finding the distinct count
n = int(input())
s = set()
for i in range(0,n):
    s.add(input())
#print(s)
print(len(s))