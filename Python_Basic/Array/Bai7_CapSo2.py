def main() :
    N = int(input())
    A = [int(x) for x in input().split()]
    min_diff = min(abs(A[i] - A[j]) for i in range(N - 1) for j in range(i + 1 , N))
    print(min_diff)
main()