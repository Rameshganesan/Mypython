def sort_by(csv_file):
    arr1 = []
    arr2 = []
    for line in csv_file.split('\n'):
        arr1.append(line.split(','))
    print(arr1)
    for i in arr1:
       arr2.append(map(str.strip,i))
    #arr2.sort(key=lambda list:int(list[0].strip(' ')),reverse=True)
    arr2.sort(key=lambda list: (int(list[0]),list[1]))
    print(arr2)
    return 0

if __name__ == '__main__':
    csv = """1,alex,80405,13,5
    3,bob,94123,320,1.5
    2,jane,94032,35,2.8
    2,jill,94110,31.6,6.1
    5,jess,94117,48,4
    6,sam,94032,31.4,9
    7,jim,94036,35,19"""
    sort_by(csv)
