import sys
from collections import deque

n = int(sys.stdin.readline())
a = deque()

for _ in range(n):
  k = list(sys.stdin.readline().split())
  if k[0] == 'push':
    a.append(k[1])
  elif k[0] == 'pop':
    if a:
      cur = a.popleft()
      print(cur)
    else:
      print(-1)
  elif k[0] == 'size':
    print(len(a))
  elif k[0] == 'empty':
    if a:
      print(0)
    else:
      print(1)
  elif k[0] == 'front':
    if a:
      cur = a[0]
      print(cur)
    else:
      print(-1)
  elif k[0] == 'back':
    if a:
      cur = a[-1]
      print(cur)
    else:
      print(-1)