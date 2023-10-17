import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
depth = 1

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)


def DFS(v):
  global depth
  visited[v] = True
  if depth == 5:
    print(1)
    sys.exit()

  for i in graph[v]:
    if not visited[i]:
      depth += 1
      DFS(i)
      depth -= 1
      visited[i] = False

for i in range(n):
  visited = [False] * (n)
  DFS(i,0)

print(0)