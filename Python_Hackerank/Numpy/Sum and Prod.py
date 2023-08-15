import numpy
n, m = map(int, input().split())
arr = numpy.array([[int(x) for x in input().split()] for _ in range(n)])
print(numpy.prod(numpy.sum(arr, axis= 0)))