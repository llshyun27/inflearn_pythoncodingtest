n = int(input())
m = list(map(int,input().split()))
number =[0 for _ in range(n)]
lr =[]
if m[0] > m[-1]:
    lr.append("R")
    number.append(m[-1])
    m.pop()
if  m[0] < m[-1]:
    lr.append("L")
    number.append(m[0])
    m.pop(0)
while(m):
    if m[0] < number[-1] and m[-1] < number[-1]:
        break
    if m[0] > number[-1] and m[-1] > number[-1] and m[0] > m[-1]:
        lr.append("R")
        number.append(m[-1])
        m.pop()
    if m[0] > number[-1] and m[-1] > number[-1] and m[0] < m[-1]:
        lr.append("L")       
        number.append(m[0])
        m.pop(0)
    if m[0] < number[-1] and m[-1] > number[-1]:
        lr.append("R")
        number.append(m[-1])
        m.pop()
    if m[0] > number[-1] and m[-1] < number[-1]:
        lr.append("L")
        number.append(m[0])
        m.pop(0)
print(len(lr))
for i in lr:
    print(i,end="")