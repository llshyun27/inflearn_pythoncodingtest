stick =list(input())
stack =[]
cnt = 0
l =len(stick)
for i in range(l):
    if stick[i] =='(':
        stack.append(stick[i])
    else: #닫는 괄호
        if stick[i-1] =='(':
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1
print(cnt)