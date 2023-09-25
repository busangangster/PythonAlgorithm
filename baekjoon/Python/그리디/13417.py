import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  dq = deque()
  a = list(input().strip().split())
  dq.append(a[0])
  for i in range(1,len(a)):
    if a[i] > dq[0]:
      dq.append(a[i])
    else:
      dq.appendleft(a[i])

  for i in range(len(dq)):
    if i == len(dq)-1:
      print(dq[i])
    else:
      print(dq[i],end='')