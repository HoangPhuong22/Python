N = int(input())
A = list(map(int , input().split()))
K = int(input())
num_dict = {}
sum = 0
for x in A:
    res = K - x
    if res in num_dict:
        sum += num_dict[res]
    if x in num_dict:
        num_dict[x] += 1
    else : num_dict[x] = 1
print(sum)