N = int(input())
A = list(map(int , input().split()))
diff = {}
diff[0] = 1
sum = 0
ans = 0
for i in A:
    sum += i
    sum = (sum % N + N) % N
    if sum in diff :
        ans += diff[sum]
    if sum in diff: diff[sum] += 1
    else : diff[sum] = 1
print(ans)