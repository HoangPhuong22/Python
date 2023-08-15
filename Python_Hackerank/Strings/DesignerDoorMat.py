n , m = map(int , input().split())
name = '.|.'
for i in range(1 , n//2 + 1):
    print((name * (i * 2 - 1)).center(m , '-'))
print('WELCOME'.center(m , '-'))
for i in range(n//2 , 0 , -1):
    print((name * (i * 2 - 1)).center(m , '-'))