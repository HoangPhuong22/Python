n = int(input())
a = list(map(int , input().split()))
print(min(a[i + 1] - a[i] for i in range(n - 1)))