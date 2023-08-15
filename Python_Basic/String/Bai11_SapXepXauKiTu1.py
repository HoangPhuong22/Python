A = input().split()
print(*sorted(A))
print(*sorted(A , lambda x: len(x)))