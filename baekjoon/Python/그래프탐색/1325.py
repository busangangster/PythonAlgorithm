

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
ans = []
for _ in range(m):
  a,b = map(int,input().split())
  graph[b].append(a)

def BFS(v):
  cnt = 1
  dq = deque()
  dq.append(v)
  visited = [False] * (n+1)
  visited[v] = True

  while dq:
    x = dq.popleft()
    for i in graph[x]:
      if not visited[i]:
        visited[i] = True
        cnt +=1
        dq.append(i)
  return cnt

for i in range(1,n+1):
  ans.append(BFS(i))

for i in range(n):
  if ans[i] == max(ans):
    print(i+1,end=' ')





