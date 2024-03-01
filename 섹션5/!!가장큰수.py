num,m = map(int,input().split()) #5276823 3
num = list(map(int,str(num)))
stack =[]
for x in num:
    while stack and m>0 and stack[-1]<x: #처음엔 stack 비어 있어 실행x, 2번째는 5<2 아니므로 실행x, 3번째는 2<7이므로 실행, 4번째 5<7이므로 실행
        #5번째는 stack 비어 있어서 실행x, , 7<6 아니므로 실행x, 6<8이므로 실행, m =0이므로 실행x
        stack.pop() #2pop, 5pop, 6pop
        m-=1 # m=2, m=1, m=0
    stack.append(x) #5append(pop),2append(pop), 7append, 6append(pop), 8append, 2append, 3append
if m!=0:
    stack = stack[:-m] #남은 m개의 숫자만큼 스택의 끝에서 제거
res =''.join(map(str,stack)) #join은 문자열 합치는데 사용, ''는 빈자리 없이 연결
#map(str, stack)은 stack 리스트의 각 숫자를 문자열로 변환한 새로운 이터레이터(iterator)를 반환
print(res) #출력