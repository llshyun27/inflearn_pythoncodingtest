#s번째부터 e번째까지의 수를 오름차순 정렬했을 때 k번째로 나타나는 수 출력
t = int(input()) #테스트케이스 수
m=1
for _ in range(t):
    n,s,e,k = map(int,input().split())
    number = list(map(int,input().split()))
    sortednumber =[]
    for i in range(s-1,e):
        sortednumber.append(number[i])
    sortednumber.sort()
    print('#%d %d' % (m,sortednumber[k-1]))
    m =m+1