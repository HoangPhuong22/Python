import re
regex = r"([a-zA-Z0-9])\1+"
matchs = re.findall(regex,input())
try :
    print(matchs[0])
except IndexError : 
    print(-1)