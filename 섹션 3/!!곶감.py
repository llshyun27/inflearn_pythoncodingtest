n = int(input())  #5
a = [0 for _ in range(n)]
for i in range(n):
    a[i] = list(map(int,input().split()))

m = int(input())  #3
for i in range(m):
   h,t,k= map(int,input().split())
   if t == 0:
       for _ in range(k):
           a[h-1].append(a[h-1].pop(0))  #맨 처음 값을 pop 해서 빼준후 맨 마지막에 넣기
   else:
       for _ in range(k):
           a[h-1].insert(0,a[h-1].pop())  #insert 활용해 0번 인덱스에 pop해서 마지막값 뺀값 넣기
res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s,e+1):
        res += a[i][j] 
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)
