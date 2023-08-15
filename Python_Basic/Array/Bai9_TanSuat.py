# def main():
#     N = int(input())
#     A = list(map(int , input().split()))
#     for i in range(N):
#         if all(A[i] != A[j] for j in range(i - 1)) : 
#             ans = 0
#             for j in range(i , N):
#                if A[i] == A[j] : ans += 1
#             print(A[i] , ans)
# main()
N = int(input())
A = list(map(int , input().split()))
my_dict = {}
for i in A :
    if i in my_dict : my_dict[i] += 1
    else: my_dict[i] = 1
for i in A:
    if my_dict[i] != 0:
        print(i , my_dict[i])
        my_dict[i] = 0