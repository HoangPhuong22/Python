from itertools import groupby
print(*[(len(list(second)) ,int(item)) for item , second in groupby(input())])