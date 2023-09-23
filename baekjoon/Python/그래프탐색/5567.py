import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
ans = [0] * (n+1)

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def BFS(v):
  dq = deque()
  dq.append(v)
  visited[v] = True 

  while dq:
    cur = dq.popleft()
    for i in graph[cur]:
      if not visited[i]:
        visited[i] = True
        dq.append(i)
        ans[i] = ans[cur] + 1

visited = [False] * (n+1)
BFS(1)
cnt = 0
for x in ans:
  if 1 <= x <= 2:
    cnt += 1
print(cnt)