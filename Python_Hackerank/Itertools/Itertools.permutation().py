import itertools
my_string , pos = input().split()
pos = int(pos)
perms = itertools.permutations(my_string , pos)
for i in sorted(perms) :
    print(*i , sep = '')