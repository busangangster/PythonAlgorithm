import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
  dq = deque()
  dq.append([v,0])
  visited[v] = True

  while dq:
    x,d = dq.popleft()
    ans[x] = d
    
    for i in graph[x]:
      if not visited[i]:
        visited[i] = True
        dq.append([i,d+1])

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = [0] * (n+1)
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

BFS(1)

max_num = max(ans)
print(ans.index(max(ans)),max(ans),ans.count(max(ans)))