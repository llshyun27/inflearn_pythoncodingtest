#n의 약수들 중 k번째로 작은 수를 출력한다. 
n,k = map(int,input().split())
number =[]
j = 0
for i in range(1,n+1):
   if (n % i == 0):
      number.append(i)
      j = j+1
if (k-1 >len(number)):
   print(-1)
else:
   print(number[k-1])  