n = int(input())
a = set(map(int , input().split()))
query = int(input())
for i in range(query):
    tt,*line = input().split()
    if tt == 'pop':
        if len(a) != 0 : a.pop()
    elif tt == 'remove':
        x = int(line[0])
        if x in a : a.remove(x)
    else :
        x = int(line[0])
        a.discard(x)
print(sum(a))