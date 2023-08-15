for i in range(int(input())):
    N = int(input())
    A = set(map(int , input().split()))
    M = int(input())
    B = set(map(int , input().split()))
    print(B.issuperset(A))
    