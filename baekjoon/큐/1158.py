import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
a = deque(range(1,n+1))
ans = []

for _ in range(n):
  for _ in range(k-1):
    cur1 = a.popleft()
    a.append(cur1)
  cur2 = a.popleft()
  ans.append(cur2)

print('<',end='')
for x in ans:
  if x == ans[-1]:
    print(x,end='')
  else:
    print(x,end=', ')
print('>')