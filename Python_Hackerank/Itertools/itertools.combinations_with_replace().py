import itertools
iterable , r = input().split()
r = int(r)
iterable = str(''.join(sorted(list(iterable))))
combiwr = itertools.combinations_with_replacement(iterable , r)
for i in combiwr:
    print(*i , sep = '')