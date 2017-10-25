def find_missing(x):
    y = []
    missing = []
    flag = False
    for i in range(0,len(x)-1):
        # print(i)
        # print(x[i]-x[i-1])
        diff = abs(x[i+1]-x[i])
        print(diff)
        if diff < 0:
            flag = True
        y.insert(i,abs(diff))
    print(y)
    print(flag)
    diff = min(y)

    for j in range(x[0],x[len(x)-1]+1,diff):
        if j not in x:
             missing.insert(j,j)
    return missing


if __name__ == '__main__':
    print('testing starts')
    a = [-2,-6,-10,-12]
    b = [3,6,9,12,18,21,27]
    print(find_missing(a))
    print(find_missing(b))