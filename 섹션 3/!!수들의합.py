n,m = map(int,input().split())
number = list(map(int,input().split()))
cnt = 0
lt = 0
rt = 1
tot = number[0]
while True:
    if tot < m: # 더한 값이 원하는 값(m)보다 작은 경우
        if rt < n :  #rt = n 이면 모든 숫자를 다 더한 것이다.
            tot += number[rt] 
            rt += 1
        else :
            break
    elif tot == m: #더한 값이 원하는 값(m)과 같은 경우
        cnt += 1 #cnt 값을 하나 증가시킴
        tot -= number[lt] 
        lt +=1
    else:
        tot -= number[lt] #더한 값이 원하는 값(m)보다 큰 경우
        lt +=1
print(cnt)