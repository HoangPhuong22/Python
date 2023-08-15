def minion_game(string):
    count_kevin , count_stuart = 0 , 0
    for i in range(len(string)):
        if s[i].lower() in "aeoui":
            count_kevin += len(string) - i
        else : count_stuart += len(string) - i
    if count_kevin > count_stuart:
        print("Kevin" , count_kevin)
    elif count_kevin < count_stuart: print("Stuart" , count_stuart)
    else : print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)