import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
  dq = deque()
  dq.append([v,0])
  visited[v] = True

  while dq:
    x,y = dq.popleft()

    if x == b:
      return y

    for i in graph[x]:
      if not visited[i]:
        visited[i] = True
        dq.append([i,y+1])
  return -1 

a,b = map(int,input().split())
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
  t,k = map(int,input().split())
  graph[t].append(k)
  graph[k].append(t)

print(BFS(a))

