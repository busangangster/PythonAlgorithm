# 0의 개수를 구하려면 숫자에 10이 곱해진 횟수를 구해줘야 함
# 10을 소인수분해하면 2*5
# 즉 5가 2보다 크기 때문에 5가 몇개 들어있는지 구해주면 됨 

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  cnt = 0
  i = 5
  while i <= n:
    cnt += n // i
    i *= 5
  print(cnt)
