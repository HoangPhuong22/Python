n = int(input())
m = 2 * n - 1
z = (m + 1) / 2
top = [('H' * (i * 2 - 1)).center(m , ' ') for i in range(1 , n + 1)]
print(*top , sep = '\n')
string = 'H'*n
for _ in range(n + 1):
    print(string.center(m , ' ') + string.rjust(6*n - 1 - m - (m - n)//2 , ' '))
for _ in range((n + 1)//2):
    print((string*5).center(6*n - 1 , ' '))
for _ in range(n + 1):
    print(string.center(m , ' ') + string.rjust(6*n - 1 - m - (m - n)//2 , ' '))
for i in range(m , 0 , -2):
    print(' '*4*n + (i*'H').center(m , ' '))
    
