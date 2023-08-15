A = input().split()
my_set = set()
B = []
for item in A :
    if item not in my_set and (item == item[::-1]):
        B.append(item)
        my_set.add(item)
print(*sorted(B , key = len))