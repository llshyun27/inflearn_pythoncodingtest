n = int(input())
correction = list(map(int,input().split())) 
score = 0
result =0
i =0
for i in range(n):
    if correction[i] ==1:
        score += 1
    else:
        score =0
    result = result +score
print(result)