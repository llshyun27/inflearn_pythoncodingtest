n = int(input())
a = []
for _ in range(n):
    h,w = list(map(int,input().split()))
    a.append((h,w))
a.sort(reverse = True)
largest =0
cnt =0 #씨름선수로 뽑히는 최대인원
for x,y in a:
    if y > largest: #내려가면서 제일 큰애가 largest가 됨.
        largest = y
        cnt += 1
print(cnt)
