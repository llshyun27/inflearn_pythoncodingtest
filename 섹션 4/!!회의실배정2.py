#동시에 진행가능한 회의의 최대 수
n = int(input()) #회의수
meeting =[]
for _ in range(n):
    s,e = list(map(int,input().split()))
    meeting.append((s,e))
meeting.sort(key = lambda x : (x[1],x[0])) #e값으로 정렬하는 람다함수,(x[1],x[0])이 리턴값

et = 0 #현재까지 진행된 회의 중 가장 늦게 끝나는 회의의 종료시간
cnt = 0 #현재까지 진행된 회의의 수
for s,e in meeting:
    if s >= et:  #다음 회의 시작시간(s)이 현재 회의 종료시간(et)보다 늦을 경우에만 새로운 회의 진행가능
        et = e #최종 회의 종료시간(et)는 현재회의 종료시간(e)
        cnt +=1 #진행된 회의 수 추가
print(cnt)
