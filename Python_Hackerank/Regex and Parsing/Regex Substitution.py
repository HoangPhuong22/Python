import re
parten = r'(?<= )&&(?= )|(?<= )\|\|(?= )'
for _ in range(int(input())):
    print(re.sub(parten, lambda x: 'and' if x.group() == '&&' else 'or' , input()))