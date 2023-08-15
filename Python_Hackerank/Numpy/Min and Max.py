import numpy as np
n, m = map(int, input().split())
arr = np.array([[int(x) for x in input().split()] for _ in range(n)])
print(max(np.min(arr, axis=1)))