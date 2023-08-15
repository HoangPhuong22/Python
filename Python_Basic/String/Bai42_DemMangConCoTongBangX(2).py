N,X = map(int, input().split())
A = list(map(int , input().split()))
diff = {}; diff[0] = 1; sum = 0; ans = 0
for i in A:
    sum += i
    if (sum - X) in diff:
        ans += diff[sum - X]
    if sum in diff:
        diff[sum] += 1
    else: diff[sum] = 1
print(ans)