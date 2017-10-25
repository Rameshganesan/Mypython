if __name__ == '__main__':
    x = 3
    y = 3
    z = 3
    n = 6
    print([[i,j,k] for i in range(1,x+1) for j in range(1,y+1) for k in range(1,z+1) if i + j + k == n])
