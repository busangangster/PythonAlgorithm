

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  j,n = map(int,input().split())
  box = []
  cnt = 0
  for _ in range(n):
    a,b = map(int,input().split())
    box.append(a*b)

  # 크기가 가장 큰 상자에 사탕을 먼저 채우기 위해
  box.sort(reverse = True) 

  for i in box:
    if j > i: # 남은 사탕의 수가 박스 크기보다 클 때
      j -= i
      cnt += 1
    else: # 남은 사탕의 수가 박스 크기랑 같거나 작을 때
      cnt += 1 # 남은 사탕을 담아야 하기 때문에 cnt + 1 
      print(cnt)
      break
      

