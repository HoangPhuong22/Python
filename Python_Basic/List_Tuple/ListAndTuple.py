import math
N = int(input())
A = [tuple(map(int,input().split())) for _ in range(N)]
my_dis = [math.sqrt(x**2 + y**2) for x , y in A]
# print(*[f"{x:.2f}" for x in my_dis] , end = '\n')
print(*["{:.2f}".format(x) for x in my_dis])