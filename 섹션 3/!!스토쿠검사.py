def check(a):
    for i in range(9):
        ch1 =[0] * 10 #행을 체크
        ch2 = [0] * 10 #열을 체크
        for j in range(9):
            ch1[a[i][j]] =1 #1~9가 모두 있는지 체크, 있으면 1 넣기
            ch2[a[j][i]] =1 #1~9가 모두 있는지 체크, 있으면 1 넣기
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 =[0] * 10  # 3*3칸 체크
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] =1
            if sum(ch3)!=9:
                return False
    return True

a = [list(map(int,input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("No")