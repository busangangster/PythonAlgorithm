import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(v):
  global cnt
  visited[v] = True
  a[v] = cnt

  for x in graph[v]:
    if not visited[x]:
      cnt += 1
      DFS(x)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
a = [0] * 100001
cnt = 1
visited = [False] * (n+1)

for _ in range(m):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

for x in graph:
  x.sort()

DFS(r)
for i in range(1,n+1):
  print(a[i])