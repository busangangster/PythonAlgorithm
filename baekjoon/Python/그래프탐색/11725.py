import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
ans = [0] * (n+1)

for _ in range(n-1):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def BFS(v):
  dq = deque()
  dq.append(v)
  visited[v] = True

  while dq:
    f = dq.popleft()
    for i in graph[f]:
      if not visited[i]:
        visited[i] = True
        ans[i] = f
        dq.append(i)

visited = [False] * (n+1)
BFS(1)
for i in range(2,n+1):
  print(ans[i])
