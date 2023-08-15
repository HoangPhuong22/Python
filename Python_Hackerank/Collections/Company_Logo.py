import collections
import functools
def cmp(a , b):
    if a[1] != b[1] : return b[1] - a[1]
    else : return ord(a[0])- ord(b[0])
s = input()
my_list = []
diff = collections.defaultdict()
for i in s:
    diff[i] = diff.get(i , 0) + 1
for item , second in diff.items():
    my_list.append([item , second])
my_list.sort(key = functools.cmp_to_key(cmp))
for _ in range(3):
    print(my_list[_][0] , my_list[_][1])