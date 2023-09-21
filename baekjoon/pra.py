import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def BFS(start): # 간선 확인
  visited[start] = True
  dq = deque()
  dq.append(start)

  while dq:
    v = dq.popleft()
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        dq.append(i)

visited = [False] * (n+1)
cnt = 0

for i in range(1,n+1): # 연결선 확인
  if not visited[i]:
    if not graph[i]:
      cnt += 1
      visited[i] = True
    else:
      BFS(i)
      cnt += 1

print(cnt)
