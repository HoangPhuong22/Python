import numpy
n, m, p = map(int, input().split())
arr1 = numpy.array([[int(x) for x in input().split()] for _ in range(n)])
arr2 = numpy.array([[int(x) for x in input().split()] for _ in range(m)])
print(numpy.concatenate((arr1, arr2)))