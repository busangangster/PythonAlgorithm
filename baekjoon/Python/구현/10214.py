import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  y = 0
  k = 0
  for _ in range(9):
    a,b = map(int,input().split())
    y += a
    k += b
  
  if y > k:
    print('Yonsei')
  elif k > y:
    print('Korea')
  elif y == k:
    print('Draw')
    