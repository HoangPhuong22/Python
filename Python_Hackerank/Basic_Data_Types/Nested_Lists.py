if __name__ == '__main__':
    my_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        my_list.append((name , score))
    min_score = min(y for x , y , in my_list)
    min_two_score = min(y for x , y in my_list if y != min_score)
    print(*sorted([x for x,y in my_list if y == min_two_score]) , sep = '\n')