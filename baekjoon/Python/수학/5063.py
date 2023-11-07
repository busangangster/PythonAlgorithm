import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  a,b,c = map(int,input().split())
  if b - a > c:
    print('advertise')
  elif b - a == c:
    print('does not matter')
  else:
    print('do not advertise')