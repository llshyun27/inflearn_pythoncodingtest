n = int(input())
m =[0 for _ in range(n+2)]
m[0] = [0 for _ in range(n+2)]
m[n+1] = [0 for _ in range(n+2)]
count =0
for i in range(1,n+1):
    m[i] = list(map(int, input().split()))
for i in range(1,n+1):    
    m[i].append(0)
    m[i].insert(0,0)
for i in range(1,n+1):  #and 사용해도 ok!
    for j in range(1,n+1):
        if m[i-1][j] < m[i][j] :
           if m[i+1][j] < m[i][j] :
               if m[i][j+1] <m[i][j]:
                  if m[i][j-1]<m[i][j]:
                    count +=1
print(count)