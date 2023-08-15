def main():
    N = int(input())
    A = [(tuple(map(int, input().split()))) for _ in range(N)]
    my_sum = [x + y + z for x , y , z in A]
    print(*[x for x in my_sum] , sep = ' ')
if __name__ == '__main__':
    main()