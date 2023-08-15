n ,m = map(int,input().split())
arr = list(map(int , input().split()))
a = list(map(int , input().split()))
b = list(map(int , input().split()))
diff = {}
for num in arr : 
    if num in diff :diff[num] += 1
    else : diff[num] = 1
my_sum = 0
my_sum += sum(diff.get(x , 0) for x in a)
my_sum += sum(-diff.get(x , 0) for x in b if x in diff)
print(my_sum)
