#6. Write a python script which takes a three digit number from the user and displays
#    only its middle digit.

import math
def middledigit(n):
    digits=math.log10(n)+1;
    n=int((n//math.pow(10,digits//2)))%10;
    return n;
print(middledigit(12354))
