import sys

def palind(ptext):
   pal=''
   for i in range(len(ptext)-1,-1,-1):
       pal=pal+ptext[i]
   return pal

if __name__ == "__main__":
    k = palind('SAS')
    if ( k == 'SAS'):
        print('Its a palindrome')
    else:
        print('Its not a palindrome')
