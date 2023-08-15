import math
AB = float(input())
BC = float(input())
MC = math.sqrt(AB ** 2 + BC ** 2) 
print(f'{round(math.degrees(math.acos(BC / MC)))}' + "\N{DEGREE SIGN}")