import sys
input = sys.stdin.readline

x,y = map(int,input().split())

# x와 y중 더 작은 값을 찾아서, 그 값을 10으로 나눈 몫을 더하면 됨.
if x <= y: 
  t = x // 10
  print(x + y + t)
else:
  t = y // 10
  print(x + y + t)
  


