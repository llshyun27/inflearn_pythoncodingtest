a = [list(map(int,input().split())) for _ in range(7)]
cnt =0
for i in range(3): #0,1,2만 돈다. 3부터는 어차피 뒤에 5개가 남아있지 않는다.
    for j in range(7):  #가로로 검사
        tmp = a[j][i:i+5] #a[0~6][0~3:1~6]
        if tmp == tmp[::-1]:  #회문이 같으면
           cnt +=1
        for k in range(2):  #5자리 이므로 2번만 검사하면 된다.
            if a[i+k][j]!=a[i+5-k-1][j]:
                break
        else:  #정상적으로 회문이 끝났다면
            cnt+=1
print(cnt)