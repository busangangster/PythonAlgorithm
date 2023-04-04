

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
degree = [0] * (n+1)
dq = deque()

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  degree[b] += 1

for i in range(1,n+1):
  if degree[i] == 0:
    dq.append(i)

while dq:
  x = dq.popleft()
  print(x,end=' ')
  for i in graph[x]:
    degree[i] -= 1
    if degree[i] == 0:
      dq.append(i)