import itertools
A = list(map(int , input().split()))
B = list(map(int , input().split()))
Result = list(itertools.product(A, B))
print(*Result)