def Count(capacity):
    cnt =1
    sum =0
    for x in music:
        if sum + x > capacity: #x곡은 이 cd에 저장할 수 없음
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

n,m = map(int,input().split())
music= list(map(int,input().split()))
result =0
lt = 1
rt = sum(music)  #45
while lt <= rt: 
    mid = (lt+rt)//2   #23
    if Count(mid) <=m:
        result = mid
        rt = mid-1
    else:
        lt = mid+1
print(result)