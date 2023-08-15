import re
for i in range(int(input())) : 
    number = input()
    regex = r"^[+-]?[0-9]*\.[0-9]+$"
    print(re.fullmatch(regex , number) is not None)