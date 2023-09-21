import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def BFS(v):
  visited[v] = True
  dq = deque()
  dq.append(v)

  while dq:
    cur = dq.popleft()
    for i in graph[cur]:
      if not visited[i]:
        visited[i] = True
        dq.append(i)

for i in range(1,n+1):
  if not visited[i]:
    if not graph[i]:
      cnt += 1
      visited[i] = True

    else:
      BFS(i)
      cnt += 1

print(cnt)



