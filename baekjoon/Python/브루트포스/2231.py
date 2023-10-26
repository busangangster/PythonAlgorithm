import sys
input = sys.stdin.readline

n = int(input())

for i in range(1,n+1):
  t = str(i) # 자릿수를 더하기 위해 str로 변환
  cur = i
  for x in t:
    cur += int(x) 
  if cur == n: # 생성자 가능한지 확인
    print(i) # 가능하면 출력 and break
    break

else: # for문이 정상종료 되면 생성자 X => 0출력
  print(0)