import collections
N = int(input())
Student = collections.namedtuple('Student' , input().split())
print('{:.2f}'.format(sum(float(Student(*input().split()).MARKS) for _ in range(N)) / N))