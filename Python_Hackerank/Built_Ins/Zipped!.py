n, m = map(int , input().split())
result = [sum(i) / len(i) for i in zip(*[list(map(float, input().split())) for _ in range(m)])]
print(*result , sep = '\n')