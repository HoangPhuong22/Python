n , x = map(int , input().split())
a =list(map(int ,input().split()))
my_dict = {}
sum , ans = [0 , 0]
my_dict[0] = 1
for i in a :
    sum += i
    if (sum - x) in my_dict:
        ans += 1
    my_dict[sum] = 1
print(ans)
        