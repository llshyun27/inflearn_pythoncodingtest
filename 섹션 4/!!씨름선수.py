n = int(input())
player = []
for i in range(n):
    h,w = list(map(int,input().split()))
    player.append((h,w))
player.sort(reverse =True)
print(player)
largest = 0
cnt = 0
for x, y in player:
    if y > largest: 
        largest =y
        cnt +=1
print(cnt)