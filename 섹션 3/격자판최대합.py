n = int(input())
number = [0 for _ in range(n)]
for i in range(n):
    number[i] = list(map(int,input().split()))


#가로로 모두 더하기
w = [0 for _ in range(n)]
for i in range(n):
    w[i] = sum(number[i])
a = max(w)
#세로로 모두 더하기
l = [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        l[i] = l[i] + number[j][i]
b = max(l)
#대각선으로 모두 더하기
k = [0,0]
for i in range(n):
    k[0] = k[0] + number[i][i]

for i in range(n):
    k[1] = k[1] + number[n-i-1][i]
c = max(k)
print(max(a,b,c))