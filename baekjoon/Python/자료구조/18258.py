import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()

for _ in range(n):
  a = input().strip().split()
  if a[0] == 'push':
    dq.append(a[1])
  elif a[0] == 'pop':
    if dq:
      print(dq.popleft())
    else:
      print(-1)
  elif a[0] == 'size':
    print(len(dq))
  elif a[0] == 'empty':
    if dq:
      print(0)
    else:
      print(1)
  elif a[0] == 'front':
    if dq:
      print(dq[0])
    else:
      print(-1)
  else:
    if dq:
      print(dq[-1])
    else:
      print(-1)

