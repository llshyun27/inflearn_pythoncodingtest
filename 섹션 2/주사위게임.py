n = int(input())
score =[]
result =[0] *(n+1)
for i in range(n):
    score.append(list(map(int,input().split())))

for i in range(n):
    if score[i][0] == score[i][1]== score[i][2]:
        result[i] = 10000 + score[i][0] *1000
    elif score[i][0] ==score[i][1] !=score[i][2] |score[i][0] ==score[i][2] !=score[i][1]:
        result[i] = 1000 + score[i][0] *100
    elif score[i][1]==score[i][2] !=score[i][0]:
        result[i] = 1000 + score[i][1] *100
    else:
        result[i] = max(score[i])*100

print(max(result))