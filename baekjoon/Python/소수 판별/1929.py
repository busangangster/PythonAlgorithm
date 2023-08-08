# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

a, b = map(int,input().split())

for i in range(a,b+1):
  if i == 1: # i가 1일 때 확실히 체크해줘야 함 
    continue
  for j in range(2,int(i**0.5)+1): 
    if i%j == 0:
      break
  else: # for문이 break 없이 정상적으로 끝났을 때, i를 출력
    print(i)


