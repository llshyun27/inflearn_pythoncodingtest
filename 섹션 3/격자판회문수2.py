n =[0 for _ in range(7)]
l =[]
w = [[] for _ in range(7)]
count = 0
for i in range(7):
    n[i] = list(map(int,input().split()))
#가로로 5자리 찾기
for i in range(7):
   for j in range(3):
       l.append(n[i][j:j+5])
for i in range(21):
    if l[i][0] == l[i][4] and l[i][1] ==l[i][3]:
        count+=1
#세로로 찾기
for i in range(7):
    for j in range(3):
        w[i].append(n[j][i])
        w[i].append(n[j+1][i])
        w[i].append(n[j+2][i])
        w[i].append(n[j+3][i])
        w[i].append(n[j+4][i])
for i in range(7):
    for j in range(0,11,5):
        if w[i][j]==w[i][j+4] and w[i][j+1] ==w[i][j+3]:
            count+=1
print(count)