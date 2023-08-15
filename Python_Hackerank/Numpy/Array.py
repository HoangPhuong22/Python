import numpy

def arrays(arr):
    arr = numpy.array(arr , float)
    arr = arr[::-1]
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)