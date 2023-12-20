import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
while True:
  k = int(input())
  if k == -1:
    break
  else:
    if k != 0:
      if len(dq) < n:
        dq.append(k)
      else:
        continue
    else:
      dq.popleft()

if not dq:
  print('empty')
else:
  print(*dq)