import re
s = input()
k = input()
match = re.finditer(f'(?=({k}))' , s)
if re.search(f'(?=({k}))' , s) is not None : 
    for i in match:
        print((i.start(1) , i.end(1) - 1))
else : print(-1, -1)