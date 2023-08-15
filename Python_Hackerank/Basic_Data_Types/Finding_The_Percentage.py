#CODE BY : Zerocoder 
#HoangPhuong-DZ
if __name__ == '__main__':
    student = {}
    for _ in range(int(input())) :
        name, *line = input().split()
        score = list(map(float , line))
        student[name] = score
    query_name = input()
    result = 0
    for i in range(3):
        result += student[query_name][i]
    result /= 3
    print('{:.2f}'.format(result))