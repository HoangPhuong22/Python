import re
parten = r'\#[a-fA-F0-9]{3,6}(?=[,;)])'
for _ in range(int(input())):
    s = input()
    match = re.findall(parten, s)
    if match : 
        print(*match , sep = '\n')