import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
dq = deque(i for i in range(1,n+1))
b = list(map(int,input().split()))
ans = []

while dq:
  k = dq.popleft()
  ans.append(k)

  if b[k-1] > 0:
    dq.rotate(-(b[k-1]-1))
  else:
    dq.rotate(-b[k-1])

print(*ans)


