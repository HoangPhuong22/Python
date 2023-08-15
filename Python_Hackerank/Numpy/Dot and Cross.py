import numpy
n = int(input())
arr1 = numpy.array([[int(x) for x in input().split()] for _ in range(n)])
arr2 = numpy.array([[int(x) for x in input().split()] for _ in range(n)])
print(numpy.dot(arr1, arr2))