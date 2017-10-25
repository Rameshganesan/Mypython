def odd_p(list2):
    for i in range(0, len(list2), 2):
        print(list2[i]),


if __name__ == "__main__":
    a = '2342390'
    list1 = list(a)
    odd_p(list1)
