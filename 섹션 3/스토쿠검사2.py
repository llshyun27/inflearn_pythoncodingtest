s = [0 for _ in range(9)]
k = [0 for _ in range(9)]
count = 0
for i in range(9):
    s[i] = list(map(int,input().split()))
#한줄씩 검사하기
for i in range(9):
    k[i] = set(s[i])
    if len(k[i]) == 9:
        count +=1
#0~3, 0~3 검사하기
l = []
l1 =[]
count1 =0
for i in range(0,3):
    for j in range(0,3):
        l.append(s[i][j])
for i in range(9):
    l1 = set(l)
    if len(l1) ==9:
       count1 +=1
count2 =0
for i in range(0,3):
    for j in range(3,6):
        l.append(s[i][j])
for i in range(9):
    l1 = set(l)
    if len(l1) ==9:
       count2 +=1
count3 =0
for i in range(0,3):
    for j in range(6,9):
        l.append(s[i][j])
for i in range(9):
    l1 = set(l)
    if len(l1) ==9:
       count3 +=1
count4 =0
for i in range(3,6):
    for j in range(0,3):
        l.append(s[i][j])
for i in range(9):
    l1 = set(l)
    if len(l1) ==9:
       count4 +=1
count5 =0
for i in range(3,6):
    for j in range(3,6):
        l.append(s[i][j])
for i in range(9):
    l1 = set(l)
    if len(l1) ==9:
       count5 +=1
count6 =0
for i in range(3,6):
    for j in range(6,9):
        l.append(s[i][j])
for i in range(9):
    l1 = set(l)
    if len(l1) ==9:
       count6 +=1
count7 =0
for i in range(6,9):
    for j in range(0,3):
        l.append(s[i][j])
for i in range(9):
    l1 = set(l)
    if len(l1) ==9:
       count7 +=1
count8 =0
for i in range(6,9):
    for j in range(3,6):
        l.append(s[i][j])
for i in range(9):
    l1 = set(l)
    if len(l1) ==9:
       count8 +=1
count9 =0
for i in range(6,9):
    for j in range(6,9):
        l.append(s[i][j])
for i in range(9):
    l1 = set(l)
    if len(l1) ==9:
       count9 +=1
if count ==9 and count1 ==9 and count2 ==9 and count3 ==9 and count4 ==9 and count5 ==9 and count6 ==9 and count7 ==9 and count8 ==9 and count9 ==9:
    print("YES")
else:
    print("NO")