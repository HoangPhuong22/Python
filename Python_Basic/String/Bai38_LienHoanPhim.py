n = int(input())
a = list(tuple(map(int ,input().split())) for _ in range(n))
a.sort(key = lambda x : x[1])
max_first = 0; ans = 0
for x , y in a :
    if x >= max_first:
        max_first = y
        ans += 1
print(ans)
