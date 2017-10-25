from operator import itemgetter

a = ['vishu','venu','baanu','somu']
b = [41,32,23,14]

#list of tuple
a1 = zip(a,b)
print(a1)
a1.sort(key=lambda tup:tup[0])
print(a1)

#list of list
a2 = []
for i,j in zip(a,b):
     a2.append([i,j])
#print(a2)
a2.sort(key=lambda list:list[1])
print(a2)

#list of dictionary
a3 = []
for i,j in zip(a,b):
    a3.append({'Name':i, 'Age':j})
print(a3)
a3.sort(key=lambda dict:dict['Age'])
print(a3)





