n = int(input())
number = list(map(int,input().split()))
res = ""
tmp =[]
last=0
lt =0
rt =n-1
while lt<=rt:
    if number[lt]>last:
        tmp.append((number[lt],'L'))
    if number[rt]>last:
        tmp.append((number[rt],'R'))
    tmp.sort() #튜플의 첫자리 값으로 정렬을 한다.
    if len(tmp)==0: #tmp의 길이가 0이면 끝
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][0] =='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()
print(len(res))
print(res)
