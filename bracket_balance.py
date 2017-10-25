from collections import Counter

def find_missing(str):
    stack1 = []
    stack2 = []
    result = []
    res_dict = {}
    open_set = '<[{('
    closed_set = '>]})'
    a = list(str)
    for i in a:
        if i in open_set:
            stack1.append(i)
        elif i in closed_set:
            stack2.append(i)
    dict1 = Counter(stack1)
    dict2 = Counter(stack2)
    print(dict1)
    print(dict2)
    for i in open_set:
        if dict1[i] > dict2[closed_set[open_set.index(i)]]:
            res_dict[closed_set[open_set.index(i)]] = dict1[i] - dict2[closed_set[open_set.index(i)]]
            result.append(closed_set[open_set.index(i)])
    for i in closed_set:
        if dict2[i] > dict1[open_set[closed_set.index(i)]]:
            res_dict[open_set[closed_set.index(i)]] = dict2[i] - dict1[open_set[closed_set.index(i)]]
            result.append(open_set[closed_set.index(i)])
    return res_dict
    # return result

if __name__ == '__main__':
    str1 = '{This ((()bracket {[function]} <<going> crazy}'
    x = find_missing(str1)
    if len(x) > 0:
        print("Imbalanced")
        print(x)
    else:
        print("Balanced")
