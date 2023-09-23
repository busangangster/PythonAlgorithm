import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
location = [0] * (n+1)

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)

def BFS(v):
  result = []
  dq = deque()
  dq.append(v)
  visited[v] = True

  while dq:
    cur = dq.popleft()
    for i in graph[cur]:
      if not visited[i]:
        visited[i] = True
        dq.append(i)
        location[i] = location[cur] + 1
        if location[i] == k:
          result.append(i)

  if len(result) == 0:
    print(-1)
  else:
    result.sort()
    for x in result:
      print(x)

visited = [False] * (n+1)
BFS(x)