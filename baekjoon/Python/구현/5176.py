import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  p,m = map(int,input().split())
  dic = {}
  cnt = 0
  for _ in range(p):
    a = int(input())
    if a not in dic:
      dic[a] = 1
    else:
      cnt += 1
  print(cnt)