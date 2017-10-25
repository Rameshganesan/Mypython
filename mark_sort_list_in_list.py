stud = [['Kavi',45],['sunil',67],['subbu',69],['Nizam',67]]
marks = []
dict = {}
# for _ in range(int(raw_input())):
#     name = raw_input()
#     score = float(raw_input())
#     stud.append([name, score])

stud.sort(key=lambda list: list[0])
#print(stud)

stud.sort(key=lambda list: list[1])
#print(stud)

#print(stud[1][1])

for i in stud:
    dict[i[1]] = 1
print(dict)

marks = dict.keys()
marks.sort()
print(marks)
print(marks)
second_least = marks[1]

for i in range(0, len(stud)):
    if stud[i][1] == second_least:
        print(stud[i][0])
