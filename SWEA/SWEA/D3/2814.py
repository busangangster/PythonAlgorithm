from collections import deque

def DFS(v,cnt):
  global max_v
  max_v = max(max_v,cnt)
  
  for x in graph[v]:
    if not visited[x]:
      visited[x] = True
      DFS(x,cnt+1)
      visited[x] = False

t = int(input())
for t_case in range(1,t+1):
  n,m = map(int,input().split())
  max_v = -2147000000
  graph = [[] for _ in range(n+1)]

  for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
  for i in range(1,n+1):
    visited = [False] * (n+1)
    visited[i] = 1
    DFS(i,1)
  print("#{} {}".format(t_case,max_v))