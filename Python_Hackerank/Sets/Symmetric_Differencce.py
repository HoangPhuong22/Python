n = int(input())
a = set(map(int , input().split()))
m = int(input())
b = set(map(int , input().split()))
print(*sorted(set(a.symmetric_difference(b))) , sep = '\n')