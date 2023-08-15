import collections
n , m = map(int , input().split())
my_diff = collections.defaultdict(list)
for _ in range(1 , n + 1):
    character = input()
    my_diff[character].append(_)
for _ in range(m):
    character = input()
print(*my_diff[character]) if len(my_diff[character]) > 0 else print(-1)
    