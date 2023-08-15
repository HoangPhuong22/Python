import functools 
def cmp(a , b):
    return abs(a) - abs(b)
N = int(input())
A = [int(x) for x in input().split()]
# print(*sorted(A , key = functools.cmp_to_key(cmp)))
A.sort(key = functools.cmp_to_key(cmp) , reverse=False)
print(*A)
