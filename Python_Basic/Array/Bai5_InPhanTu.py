n = int(input())
a = list(x for x in input().split())
a = list(str(a[i]) for i in range(0 , len(a)) if i % 2 == 0 and a[i] % 2 == 0)

print(' '.join(a)) if len(a) > 0 else print("NONE")