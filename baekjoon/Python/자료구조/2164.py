import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(range(1,n+1))

a = deque(a)

while True:
  if len(a) == 1:
    print(a[0])
    break
  cur1 = a.popleft()
  cur2 = a.popleft()
  a.append(cur2)