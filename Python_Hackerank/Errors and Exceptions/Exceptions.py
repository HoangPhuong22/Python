import sys
for _ in range(int(input())):
    a , b = input().split()
    try : 
        print(int(int(a) //int(b)))
    except :
        ex_type , ex_value , ex_trackback = sys.exc_info()
        print("Error Code:" , ex_value)