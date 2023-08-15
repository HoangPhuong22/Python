import collections
N = int(input())
my_cltions = collections.Counter(map(int , input().split()))
query = int(input())
sum = 0
while query > 0 : 
    n , m = map(int ,input().split())
    if my_cltions[n] > 0:
        sum += m
        my_cltions[n] -= 1
    query -= 1
print(sum)