def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)

if __name__ == '__main__':
    string = input()
    position , character = input().split()
    print(mutate_string(string , int(position), character))