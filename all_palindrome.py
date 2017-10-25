def  countPalindromes(s):
    cnt = 0
    for i in range(0, len(s)+1):
        for j in range(0, len(s)+1):
            if len(s[i:j]) > 0:
                if s[i:j] == s[i:j][::-1]:
                    cnt += 1
    return cnt

if __name__ == "__main__":
    s = 'sssddd'
    print(countPalindromes(s))