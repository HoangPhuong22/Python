import itertools
K, M = map(int , input().split())
my_list = []
for _ in range(K):
    n , *item = input().split()
    my_list.append(list(map(int ,item)))
my_max = map(lambda x : sum(i*i for i in x)%M ,itertools.product(*my_list))
print(max(my_max))