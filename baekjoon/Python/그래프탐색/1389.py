import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
  dq = deque()
  dq.append(v)
  visited[v] = 1

  while dq:
    x = dq.popleft()

    for i in graph[x]:
      if not visited[i]:
        visited[i] = visited[x] + 1
        dq.append(i)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

result = []

for i in range(1,n+1):
  visited = [0 for _ in range(n+1)]
  BFS(i)
  result.append(sum(visited))

for i in range(len(result)):
  if result[i] == min(result):
    print(i+1)
    break