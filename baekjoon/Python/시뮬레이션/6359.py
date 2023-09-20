import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  p = [1 for _ in range(n+1)]
  for i in range(2,n+1):
    for j in range(i,len(p),i):
      if p[j] == 0:
        p[j] = 1
      else:
        p[j] = 0
  p.pop(0)
  print(p.count(1))
