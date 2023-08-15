N = int(input())
A = input().split()
print(*sorted(A , key = lambda x : (sum(map(int , x)) , int(x))))