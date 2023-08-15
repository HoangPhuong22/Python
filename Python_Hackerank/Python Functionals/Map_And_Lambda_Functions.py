cube = lambda x: x**3

def fibonacci(N):
    A = [] if N == 0 else ([0] if N == 1 else [0 , 1])
    [A.append(A[i - 1] + A[i - 2]) for i in range(2 , N)]
    return A

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))