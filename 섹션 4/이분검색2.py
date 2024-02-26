n ,m = map(int, input().split())
number = list(map(int,input().split()))
number.sort()
lt = 0
rt = n-1
while lt <= rt:
    mid = (lt + rt)//2
    if m == number[mid]:
        print(mid+1)
        break
    if m >= number[mid]:
        lt = mid+1
    else:
        rt = mid-1
     