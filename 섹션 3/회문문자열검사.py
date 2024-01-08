n = int(input())
for i in range(n):
   data = input()
   data = data.upper() #모두 대문자로 변환해 대소문자 구별x
   l = len(data)
   for j in range(l//2):
      if data[j] != data[l-j-1]:
         print("#%d NO" %(i+1))
         break
   else : print("#%d YES" %(i+1))