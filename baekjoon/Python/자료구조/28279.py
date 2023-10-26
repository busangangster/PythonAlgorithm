import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
dq = deque()

for _ in range(n):
  a = list(map(int,input().split()))
  if a[0] == 1:
    dq.appendleft(a[1])
  elif a[0] == 2:
    dq.append(a[1])
  elif a[0] == 3:
    if dq:
      print(dq.popleft())
    else:
      print(-1)
  elif a[0] == 4:
    if dq:
      print(dq.pop())
    else:
      print(-1)
  elif a[0] == 5:
    print(len(dq))
  elif a[0] == 6:
    if dq:
      print(0)
    else:
      print(1)
  elif a[0] == 7:
    if dq:
      print(dq[0])
    else:
      print(-1)
  elif a[0] == 8:
    if dq:
      print(dq[-1])
    else:
      print(-1)

    