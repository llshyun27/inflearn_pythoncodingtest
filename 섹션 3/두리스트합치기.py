n = int(input())
list_n = list(map(int,input().split()))
m = int(input())
list_m = list(map(int,input().split()))

for i in range(m):
    list_n.append(list_m[i])
list_n.sort()

for x in list_n:
    print(x,end =" ")