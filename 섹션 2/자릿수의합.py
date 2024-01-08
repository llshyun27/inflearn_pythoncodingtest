def digit_sum(x):
    result2 =0
    length = len(str(x))
    for i in range(length,0,-1):
        result = x // (10**(i-1))
        x = x % (10**(i-1))
        result2 = result2 + result
    return result2


n = int(input())
x = list(map(int,input().split()))
result =[]
for y in x:
    s = digit_sum(y)
    result.append(s)
a = max(result)
for i in range(n):
    if a == digit_sum(x[i]):
        print(x[i])
        break