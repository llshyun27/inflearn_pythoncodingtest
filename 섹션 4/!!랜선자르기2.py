def Count(len):
    cnt =0
    for x in line:
        cnt += (x//len)
    return cnt 

k,n = map(int,input().split())
line = []
for i in range(k):
    tmp = int(input())
    line.append(tmp)
largest = max(line)
lt = 0
rt = largest
res =0
while lt<=rt:
    mid = (lt + rt)//2
    if Count(mid) >= n:  #개수가 원하는것보다 많이 나와서 더 긴 길이가 있는지 찾기
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)