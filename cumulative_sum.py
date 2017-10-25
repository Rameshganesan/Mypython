if __name__ == "__main__":
    a = [1,2,3,4,5]
    res = []
    z = 0
    for i in range(0,len(a)):
        z = z + a[i]
        res.insert(i,z)

    print(res)

