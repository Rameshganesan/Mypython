import itertools

a = []
for perm in itertools.permutations("ted"):
    a = a + [("".join(perm))]
    #print(perm)
print(a)

