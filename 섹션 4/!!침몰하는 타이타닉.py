n,m = map(int,input().split())
weight = list(map(int,input().split()))
weight.sort()
cnt = 0
result = 0
while weight:
    #제일 무거운 사람 + 가벼운 사람 같이 태우기
    if weight[0] + weight[-1] > m: #[-1]은 제일 뒤에 사람, 둘이 m보다 클경우 같이 못탐
        weight.pop() #맨 마지막 사람 혼자 타라고 하고 리스트에서 pop
        cnt +=1  #맨 마지막 사람 혼자 탄거 추가
    else: #젤 무거운 + 젤 가벼운 사람 같이 탈 수 있음
        weight.pop(0) #젤 가벼운 사람 제거
        weight.pop() #젤 무거운 사람 제거
        cnt += 1
print(cnt)
