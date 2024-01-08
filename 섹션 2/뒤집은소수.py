def reverse(x):
    y = int(str(x)[::-1])  #정수값을 문자열로 바꿔 뒤집는 과정에 대해서 이 아이디어를 떠올려야 쉬움.
    return y

def isPrime(x):
    cnt =0
    for i in range(1,x):
        if x % i == 0:
            cnt = cnt+1
    if cnt == 1:
        return x
    else:
        return 0


n = int(input())
number = list(map(int,input().split()))
result =[]
for i in number:
    x = reverse(i)
    y = isPrime(x)
    result.append(y)

for i in range(n):
    if result[i] !=0:
        print(result[i],end =" ")