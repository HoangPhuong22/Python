import collections 
N = int(input())
my_dict = collections.OrderedDict()
for _ in range(N):
    *string , num = input().split()
    string = str(' '.join(string))
    my_dict[string] = my_dict.get(string , 0) +  int(num)
for item , second in my_dict.items():
    print(item , second)