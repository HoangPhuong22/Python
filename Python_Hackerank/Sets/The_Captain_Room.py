n = int(input())
a = list(map(int , input().split()))
my_set_one = set()
my_set_two = set()
for i in a:
    if i in my_set_one:
        my_set_two.add(i)
    else :
        my_set_one.add(i)
print(*my_set_one.difference(my_set_two))