n = int(input())
persi = [0 for _ in range(n)]
for i in range(n):
    persi[i] = list(map(int,input().split()))

m = int(input())
for i in range(m):
    h,t,k = map(int,input().split())
    if t == 0:
        for _ in range(k):
            persi[h-1].append(persi[h-1].pop(0)) #맨 처음값 빼서 뒤에 넣기
    else:
        for _ in range(k):
            persi[h-1].insert(0,persi[h-1].pop())#맨 뒤에꺼 빼서 앞에 넣기
s = 0
e = n-1
res =0
for i in range(n):
    for j in range(s,e+1):
        res += persi[i][j]
    if i < n//2:
        s = s+1
        e = e-1
    else:
        s = s-1
        e = e+1

print(res)