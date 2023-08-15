import numpy
n = int(input())
m = [[float(i) for i in input().split()] for _ in range(n)]
    
print(round(numpy.linalg.det(m),2))