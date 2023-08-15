import itertools
iterable , r = input().split()
r = int(r)
iterable = str(''.join(sorted(list(iterable))))
for i in itertools.count(1 , 1):
    if i > r : break
    combnt = itertools.combinations(iterable , i)
    for item in combnt:
        print(*item , sep = '')