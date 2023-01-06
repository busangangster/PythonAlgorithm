# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

n = int(input())
m = int(input())
sum = 0 # 합
ch = [] # 최솟값 찾기

for i in range(n,m+1):
  if i == 1:
    continue
  for j in range(2,int(i**0.5)+1):
    if i%j == 0: # i 나누기 j의 나머지가 0이라는 뜻은 약수가 존재한다는 뜻
      break
  else:
    sum += i
    ch.append(i)

# if문의 순서가 바뀌면 코드 성립 X

if not ch:
  print(-1)
else:
  print(sum)
  print(min(ch))