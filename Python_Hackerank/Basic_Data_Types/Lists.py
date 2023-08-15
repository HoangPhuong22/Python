#CODE BY : Zerocoder 
#HoangPhuong-DZ
if __name__ == '__main__':
    my_list = []
    for _ in range(int(input())):
        command , *args = input().split()
        if command =="insert":
            i , x = map(int , args)
            my_list.insert(i , x)
        elif command == "print":
            print(my_list)
        elif command == "remove":
            x = int(args[0])
            my_list.remove(x)
        elif command == "append":
            x = int(args[0])
            my_list.append(x)
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.pop()
        elif command == "reverse":
            my_list.reverse()