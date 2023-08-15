my_set = set(map(int ,input().split()))
ok = True
for i in range(int(input())):
    arr = set(map(int,input().split()))
    if my_set.issuperset(arr) == False:
        ok = False
        break
    elif len(arr) >= len(my_set):
        ok = False
        break
print(ok)