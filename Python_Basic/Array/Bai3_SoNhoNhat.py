n = int(input())
a = list(map(int , input().split()))
min = min(a)
count_min = sum(1 for x in a if x== min)
print(count_min)

