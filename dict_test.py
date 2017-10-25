dict = {}
word = 'This world is small but it is potential world'

arr1 = word.split(' ')
print(arr1)
for i in arr1:
    dict[i] = arr1.count(i)

print(dict)




