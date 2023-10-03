import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

for x in graph:
  x.sort()

def BFS(v):
  cnt = 1
  dq = deque()
  dq.append(v)
  visited[v] = 1

  while dq:
    x = dq.popleft()
    for i in graph[x]:
      if not visited[i]:
        cnt += 1
        visited[i] = cnt
        dq.append(i)

visited = [0] * (n+1)
BFS(r)
for i in range(1,len(visited)):
  print(visited[i])