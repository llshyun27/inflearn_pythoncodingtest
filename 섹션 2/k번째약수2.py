n,k = map(int,input().split())
a = []
for i in range(1,n):
    if n % i == 0:
        a.append(i)
if len(a) < k:
    print(-1)
else:
    print(a[k-1])