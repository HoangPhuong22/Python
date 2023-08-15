n = int(input())
a = (int(x) for x in input().split())

prime = list(filter(lambda x : x > 1 and all(x % i != 0 for i in range(2 , int(x**0.5) + 1)) , a))
sum_a = sum(prime) / len(prime)
print("{:.3f}".format(sum_a))
