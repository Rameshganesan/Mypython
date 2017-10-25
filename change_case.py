def changecase(s):
    k=[]

    for i in s:
        if i.isupper() == True:
            k.append(''.join(i.lower()))
        else:
            k.append(''.join(i.upper()))

    print(''.join(k))


if __name__ == '__main__':
    changecase('AnAnYa')

