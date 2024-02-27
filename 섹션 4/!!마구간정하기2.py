def Count(distance):
    cnt =1
    endpoint = s[0] #첫번째 말 배치된 곳
    for i in range(1,n):
        if s[i] - endpoint >= distance: #distance보다 큰 거리에 두번째 말 배치
            cnt +=1
            endpoint = s[i] #마지막 말이 배치된 곳 
    return cnt

n,c = map(int,input().split())
s =[]
for _ in range(n):
    a = int(input())
    s.append(a)
s.sort()
result = 0
lt = 0
rt = max(s)
while lt<=rt:
    mid = (lt + rt)//2
    if Count(mid) >= c:
        result = mid
        lt = mid+1
    else:
        rt = mid-1
print(result)