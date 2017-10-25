def swap_case(s):
    k = list(s)
    print(k)
    j = []
    for i in k:
        if (i.islower() == True):
           j.append(i.upper())
        else:
           j.append(i.lower())  
    return ''.join(j)

if __name__ == "__main__":
    a = 'PreeTHI1'
    print(swap_case(a))


