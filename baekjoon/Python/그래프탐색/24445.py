import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
  global cnt
  dq = deque()
  dq.append(v)
  visited[v] = True

  while dq:
    x = dq.popleft()
    a[x] = cnt
    cnt += 1

    for i in graph[x]:
      if not visited[i]:
        visited[i] = True
        dq.append(i)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
a = [0] * 100001
cnt = 1
for _ in range(m):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

for x in graph:
  x.sort(reverse=True)

BFS(r)

for i in range(1,n+1):
  print(a[i])