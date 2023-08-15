n = int(input())
my_set = set(map(int , input().split()))
query = int(input())
for i in range(query):
    operation_name , *num = input().split()
    arr_number = set(map(int , input().split()))
    if operation_name == 'intersection_update':
        my_set.intersection_update(arr_number)
    elif operation_name == 'update':
        my_set.update(arr_number)
    elif operation_name == 'symmetric_difference_update':
        my_set.symmetric_difference_update(arr_number)
    else:
        my_set.difference_update(arr_number)
print(sum(my_set))