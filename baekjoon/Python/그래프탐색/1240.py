import sys
from collections import deque
input = sys.stdin.readline

def BFS(v,f):
  cnt = 0
  dq = deque()
  dq.append([v,0])
  visited[v] = True

  while dq:
    x,y = dq.popleft()

    if x == f:
      return y

    for i,l in graph[x]:
      if not visited[i]:
        visited[i] = True
        dq.append([i,y+l])

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])

for _ in range(m):
  s,e = map(int,input().split())
  visited = [False] * (n+1)
  print(BFS(s,e))
