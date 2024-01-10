#가장 가까운 두 말의 거리가 최대가 되게 말을 배치
def Count(len):
    cnt = 1 #말 한마리 배치
    endpoint = stable[0]  #첫번째 말 배치된 곳
    for i in range(1,n):
        if stable[i]- endpoint >=len: #말 배치 성공
            cnt += 1
            endpoint = stable[i] #마지막 말 배치된 곳
    return cnt

n,c = map(int,input().split()) #n개의 마구간, c마리의 말
stable =[]
for _ in range(n):
    tmp =int(input())
    stable.append(tmp)
stable.sort()
lt =1 #최소거리
rt = stable[n-1] #최대거리
res =0
while lt<=rt:
    mid = (lt+rt)//2 #둘의 중간값을 최대거리로 보고 시작
    if Count(mid)>=c: #최대거리 더 늘려야함.
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)