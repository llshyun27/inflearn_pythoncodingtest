n = int(input())
m = [0 for _ in range(n)]
for i in range(n):
    m[i] = list(map(int,input().split()))

#맨위, 맨앞, 맨뒤, 맨끝에 0 삽입
m.insert(0,[0]*n) #맨 위 열 전체에 0 삽입
m.append([0]*n)  #맨 끝 열 전체에 0 삽입 
for x in m:
    x.insert(0,0)  #열마다 맨 앞에 0을 삽입한다.
    x.append(0) #열의 맨 끝마다 0을 삽입

#봉우리 개수 세기
cnt =0
for i in range(1,n+1):
    for j in range(1,n+1):
        if m[i][j] > m[i-1][j] and m[i][j]>m[i][j-1] and m[i][j]>m[i][j+1] and m[i][j]>m[i+1][j]:
            cnt +=1
print(cnt) 