if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_arr = max(arr)
    max_two = [x for x in arr if x < max_arr]
    print(max(max_two))