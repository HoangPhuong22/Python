#CODE BY : Zerocoder 
#HoangPhuong-DZ
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(sorted([[i , j , k] for i in range(x + 1) for j in range(y+ 1) for k in range(z + 1) if (i + j + k) != n] , key = lambda x : (x[0] , x[1] , x[2])))