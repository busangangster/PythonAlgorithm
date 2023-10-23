import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  a = [input().split() for _ in range(n)]
  a.sort(key = lambda x:int(x[1]))
  print(a[-1][0])

