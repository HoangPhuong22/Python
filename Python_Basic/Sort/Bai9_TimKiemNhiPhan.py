n = int(input())
a = list(map(int ,input().split()))
q = int(input())
while q > 0:
    x = int(input())
    q -=1 
    print("YES") if x in a else print("NO")