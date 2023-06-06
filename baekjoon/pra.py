import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = []
for i in range(1,n+1):
  a.append(i)

dq = deque(a)
k = []

for _ in range(n-1):
  cur1 = dq.popleft()
  cur2 = dq.popleft()
  k.append(cur1)
  dq.append(cur2)

for x in k:
  print(x,end=' ')

print(*dq)



    