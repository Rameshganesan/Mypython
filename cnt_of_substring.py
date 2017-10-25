def count_substring(string, sub_string):
    sub_l = len(sub_string)
    cnt = 0
    for i in range(0,len(string)):
        if string[i:sub_l+i] == sub_string:
            #print(string[i:(sub_l+i)])
            cnt += 1
    return cnt


if __name__ == '__main__':
    a = 'Rameame'
    b = 'ame'
    cnt = count_substring(a,b)
    print(cnt)
