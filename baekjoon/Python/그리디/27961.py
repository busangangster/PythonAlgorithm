import sys
input = sys.stdin.readline

n = int(input())
t = 1 # 고양이 수
cnt = 0 # 마법 사용 횟수

if  n == 0:
  print(0)
elif n == 1:
  print(1)
else:
  while t != n:
    if t >= n - t: # 고양이 수가 n-t보다 크거나 같으면
      t += n - t # 그 차이만큼 복제 
      cnt += 1
    else: # 고양이 수가 n-t보다 작으면
      t = t + t # 자기 자신을 복제
      cnt += 1
      
  print(cnt+1) # +1은 맨 처음 생성 마법으로 1마리 생성한 것
  


