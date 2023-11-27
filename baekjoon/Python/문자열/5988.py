import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
  s = int(input())
  if s % 2 ==0:
    print('even')
  else:
    print('odd')