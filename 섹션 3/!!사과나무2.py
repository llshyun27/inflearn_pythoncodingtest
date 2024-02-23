n = int(input())
apple = [0 for _ in range(n)]
for i in range(n):
    apple[i] = list(map(int,input().split()))
s = n//2
e = n//2
res = 0
for i in range(n):
    for j in range(s,e+1):
        res += apple[i][j] 
    if i < n//2:
        s = s-1
        e = e+1
    else:
        s = s+1
        e = e-1
print(res)