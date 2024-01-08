import math
n = int(input())
score = list(map(int,input().split()))
avg = sum(score)/n
upavg=math.ceil(avg)
dif =[]

for i in range(n):
    diff = score[i]-upavg
    abdiff = abs(diff)
    dif.append(abdiff)

result  = min(dif)

for j in range(n):
    if(result == dif[j]):
        print(upavg,j+1)
        break