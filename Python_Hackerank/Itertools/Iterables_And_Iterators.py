import itertools 
N = int(input())
my_list = input().split()
K = int(input())
my_combi = itertools.combinations(my_list , K)
ans = 0
sum = 0
for item in my_combi:
    sum += 1
    for i in item:
        if i == 'a':
            ans += 1
            break
print('{:.3f}'.format(ans / sum))