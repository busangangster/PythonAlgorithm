import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
a = deque(list(range(1,n+1)))
ans = []

while a:
  for _ in range(k-1):
    cur = a.popleft()
    a.append(cur)
  cur = a.popleft()
  ans.append(cur)
print('<',end='')
for x in ans:
  if x == ans[-1]:
    print(x,end='')
  else:
    print(x,end=', ')
print('>')