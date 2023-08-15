import bisect
n , m = map(int , input().split())
a = [int(x) for x in input().split()]
a.sort()
b = list(map(int , input().split()))
for num in b:
    pos = bisect.bisect_right(a , num)
    if pos > 0:
        print(a[pos - 1])
        a.pop(pos - 1)
    else: print(-1)