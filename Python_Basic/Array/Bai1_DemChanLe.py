def count(arr) : 
    even_nums = (x for x in arr if x % 2 == 0)
    odd_nums = (x for x in arr if x % 2 == 1)
    len_even = len(even_nums)
    len_odd = len(odd_nums)
    even_nums = (x for x in arr if x % 2 == 0)
    odd_nums = (x for x in arr if x % 2 == 1)
    sum_even = sum(even_nums)
    sum_odd = sum(odd_nums)
    return even_nums, odd_nums, sum_even, sum_odd

n = int(input())
a = (int(x) for x in input().split())
count_even , count_odd , sum_even , sum_odd = count(a)
print(count_even)
print(count_odd)
print(sum_even)
print(sum_odd)