n = int(input())
apple = [0 for _ in range(n)]
for i in range(n):
    apple[i] = list(map(int,input().split()))
an =0
s = n // 2
e = n // 2
for i in range(n):
    for j in range(s,e+1):
        an += apple[i][j]
    if i < n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(an)
