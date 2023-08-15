import collections
n = int(input())
my_queue = collections.deque()
for _ in range(n):
    operator_name , *num = input().split()
    if operator_name == 'append':
        my_queue.append(int(num[0]))
    elif operator_name == 'appendleft':
        my_queue.appendleft(int(num[0]))
    elif operator_name == 'pop':
        my_queue.pop()
    else : my_queue.popleft()
print(*my_queue)