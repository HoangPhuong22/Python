def print_rangoli(size):
    size_two = size - 1
    for i in map(abs , range(size_two , -size , -1)):
        c = 97 + i
        r = size - i
        diff = list(map(abs , range(-r + 1 , r)))
        s = [chr(c + x) for x in diff]
        print(('-'.join(s)).center(4*size - 3 , '-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)