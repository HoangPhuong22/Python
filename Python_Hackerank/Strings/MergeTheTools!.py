import textwrap
def merge_the_tools(string, k):
    my_list = textwrap.wrap(string , k)
    for string_two in my_list:
        diff_check = {}
        s = ''
        for i in string_two:
            if i not in diff_check:
                s += i
                diff_check[i] = 1
        diff_check.clear()
        print(s)
if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)