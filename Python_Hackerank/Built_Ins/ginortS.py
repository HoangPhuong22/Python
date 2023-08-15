import functools
def cmp(a , b):
    if a.isalpha() and b.isalpha() :
        if b.islower() == a.islower():
            if a > b : return 1
            else : return -1
        else : 
            if b.islower() : return 1
            else : return -1
    else : 
        if b.isdigit() == a.isdigit():
            if int(b) % 2 == int(a) % 2 : 
                return int(a) - int(b)
            else : return int(b)%2 - int(a)%2
        else :
            if b.isalpha() : return 1
            else : return -1
            
s = input()
s = list(s)
s.sort(key = functools.cmp_to_key(cmp))
print(*s , sep = '')