# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.


n = int(input())
a = list(map(int,input().split()))
cnt = 0

for i in a:
  if i == 1:
    continue
  for j in range(2,int(i**0.5)+1):
    if i%j == 0:
      break
  else:
    cnt +=1

print(cnt)

