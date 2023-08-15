if __name__ == '__main__':
    n = int(input())
    A = list(map(lambda x : str(x**2) , range(n)))
    print('\n'.join(A))
