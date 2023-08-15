import re
match = re.findall(r'(?<=[^AEIOUaeiou\+\-])[AEIOUaeiou]{2,}(?=[^AEIOUaeiou\+\-])' , input())
print('\n'.join(match)) if len(match) > 0 else print(-1)
