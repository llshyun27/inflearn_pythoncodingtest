l = int(input())
box = list(map(int,input().split()))
m = int(input())
box.sort() #14 40 42 65 76 81 87 
for _ in range(m):
    box[0] +=1
    box[l-1] -=1
    box.sort()
print(box[l-1]-box[0])