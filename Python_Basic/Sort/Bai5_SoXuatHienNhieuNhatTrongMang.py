N = int(input())
A = (int(x) for x in input().split())
num_dict = {}
for i in A:
    if i in num_dict:
        num_dict[i] += 1
    else : num_dict[i] =1
max_count = max(num_dict.values())
A = [num for num , second in num_dict.items() if second == max_count]
A.sort()
print(A[0] , max_count)
