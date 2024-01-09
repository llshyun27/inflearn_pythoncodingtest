#k개의 랜선을 가지고 있는데 모두 같은 길이를 가진 n개의 랜선을 만들고 싶다
#만들 수 있는 랜선의 최대길이를 구하여라
def Count(len):
    cnt =0
    for x in line:
        cnt +=(x//len)
    return cnt

k,n = map(int,input().split()) #k는 이미 가진 랜선의 수, n은 필요한 랜선의 수
line =[]
largest =0
for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest,tmp)
lt =1
rt = largest
while lt <=rt:
    mid = (lt+rt)//2
    if Count(mid)>=n: #답이 된다.-> 더 긴 길이가 있는지 찾아본다. 
        res = mid
        lt = mid+1
    else: #끈의 개수가 n이 되지 않는다. -> 더 짧게 잘라야 한다.
        rt = mid -1 #지금 mid 도 답이 되지 않으므로 더 긴 것들은 답이 될 수 없다.
print(res)