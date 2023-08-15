import math
import os
import random
import re
import sys
def solve(s):
    my_list = s.split(' ')
    for i in range(0 , len(my_list)):
        my_list[i] = my_list[i].capitalize()
    return ' '.join(my_list)
if __name__ == '__main__':
    s = input()
    print(solve(s))