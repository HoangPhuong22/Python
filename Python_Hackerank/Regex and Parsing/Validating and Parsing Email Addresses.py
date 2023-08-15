import re
parten = r'[a-zA-Z]+\s<[a-z]+[\w._-]*@[a-z]+\.[a-z]{1,3}>'
for _ in range(int(input())):
    s = input()
    if re.search(parten,s) is not None:
        print(s)