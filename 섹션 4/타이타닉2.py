n,m = map(int,input().split())
weight = list(map(int,input().split()))
weight.sort() #50 60 70 90 100
cnt = 0
while weight:
    if weight[0] + weight[-1] > m: #-1이 제일 무거운 사람 
        weight.pop() #맨 무거운 사람 혼자 타라고 하고 pop하기
        cnt+=1 #젤 무거운 사람 혼자 탄거 추가
    else: #젤 무거운사람 + 젤 가벼운 사람 같이 태우기
        weight.pop(0) #젤 가벼운 사람 제거
        weight.pop() #젤 무거운 사람 제거
        cnt+=1
print(cnt)
