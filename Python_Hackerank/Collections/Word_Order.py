import collections
n  = int(input())
my_diff = {}
for _ in range(n):
    name = input()
    my_diff[name] = my_diff.get(name , 0) + 1
print(len(my_diff))
print(*my_diff.values())
    