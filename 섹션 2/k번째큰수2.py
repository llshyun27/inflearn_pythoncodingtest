n,k = map(int,input().split())
number = list(map(int,input().split()))
number.sort()
result =[]
#result2 =[]
a =0
for i in range(n-2):
    for j in range(i+1,n-1):
        for l in range(j+1,n):
            result.append(number[l] + number[j]+ number[i])
result = sorted(set(result),reverse = True)
print(result[k-1])