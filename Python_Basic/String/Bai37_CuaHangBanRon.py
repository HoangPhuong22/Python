n = int(input())
a = []
for _ in range(n):
    x , y = map(int , input().split())
    a.append([x , 1])
    a.append([y , -1])
a.sort(key = lambda x : x[0])
sum = 0; my_max = 0
for x,y in a:
    sum += y
    my_max = max(sum , my_max)
print(my_max)