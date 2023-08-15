for _ in range(int(input())):
    n = int(input())
    my_list = list(map(int , input().split()))
    max_list = max(my_list)
    for i in range(n):
        if my_list[0] >= my_list[-1]:
            big = my_list.pop(0)
        else : big = my_list.pop(-1)
        
        if max_list >= big:
            max_list = big
        else : 
            print("No")
            break
    else : print('Yes')