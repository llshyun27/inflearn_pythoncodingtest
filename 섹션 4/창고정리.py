l = int(input())
box = list(map(int,input().split()))
m = int(input())
box.sort()
for _ in range(m):
    box[0]+=1
    box[l-1]-=1
    box.sort()

print(box[l-1]-box[0]) 