import sys

if __name__ == "__main__" :
     a = 'take'
     b = 'kacte'
     a_list = list(a)
     b_list = list(b)
     a_list.sort()
     b_list.sort()
     print(a_list)
     print(b_list)
     if (a_list == b_list):
         print('anagram')
     else:
         print('not a anagram')



