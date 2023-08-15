import heapq
n , m = map(int , input().split())
a = list(map(int , input().split()))
b = [int(x) for x in input().split()]
print(*heapq.merge(a , b))