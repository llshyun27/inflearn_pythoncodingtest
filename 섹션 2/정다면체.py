from collections import Counter
n,m = map(int,input().split())
a = []
b = []
c = []
for i in range(1,n+1):
    a.append(i)

for j in range(1,m+1):
    b.append(j)

for i in range(n):
    for j in range(m):
        k = a[i] + b[j]
        c.append(k)
cnt =[]
for i in range(2,n+m+1):
    count = c.count(i)
    cnt.append(count)
    
for i in range(0,m):
    if cnt[i] == n:
        print(c[i],end =' ')