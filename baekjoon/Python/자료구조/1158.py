import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
a = deque(range(1,n+1))
ans = []

for _ in range(n):
  for _ in range(k-1):
    t = a.popleft()
    a.append(t)
  j = a.popleft()
  ans.append(j)


print('<',end='')   
for x in ans:
  if x == ans[-1]:
    print(x,end='')
  else:
    print(x,end=', ')
print('>')