N = int(input())
A = [map(int , input().split())]
B = []
for i in range(N) :
    if all(A[i] != A[j] for j in range(i)):
        B.append(str(A[i]))
print(' '.join(B))