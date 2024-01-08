#n보다 작은 소수의 개수 구하기
'''
n = int(input())
cnt =[0] * (n+1)
count =0
for i in range(1,n+1):
    for j in range(2,n+1):
        if i % j == 0:
            cnt[i] = cnt[i] + 1
    if cnt[i] == 1:
        count = count +1
print(count)''' 
#내가 짠 코드는 모든 경우의 수를 다 검토해 n값이 커지면 시간이 매우 오래 걸린다

#따라서 배수의 값을 이용해 2를 포함시키고 2의 배수인 모든 값은 배열 값을 1로 지정해
#소수가 아님을 표시한다
n = int(input())
ch=[0]*(n+1)
cnt =0
for i in range(2,n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i,n+1,i):
            ch[j]=1
print(cnt)
