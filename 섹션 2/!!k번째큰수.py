#숫자의 배열 중 3장을 뽑아 더한 값중 k번째로 큰 값을 출력
n, k = map(int,input().split())
number = list(map(int,input().split()))
res = set()  # 중복 제거 리스트 res 선언
#값을 3개 뽑아서 res에 넣는다.
for i in range(n):
    for j in range(i+1,n): #i 뒤에 있는 애들만 검토해 리스트에 넣기
        for m in range(j+1,n): #j 뒤 부터 돌기(1,2,3/1,2,4/1,2,5)
            res.add(number[i]+number[j]+number[m])
res = list(res) #res를 리스트화 시킨다.
res.sort(reverse = True) #내림차순 정렬
print(res[k-1])
