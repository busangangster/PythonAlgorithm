import sys
input = sys.stdin.readline
from collections import deque

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS(a,b):
  dq = deque()
  dq.append([a,b])
  visited[a][b] = True
  cnt = 0

  while dq:
    x,y = dq.popleft()

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx <n) and (0 <= yy < m) and not visited[xx][yy]:
        if graph[xx][yy] == '#':
          visited[xx][yy] = True
          dq.append([xx,yy])

t = int(input())
for _ in range(t):
  n,m = map(int,input().split())
  graph = [list(input().strip()) for _ in range(n)]
  visited = [[False for _ in range(m)] for _ in range(n)]
  ans = 0
  for i in range(n):
    for j in range(m):
      if not visited[i][j] and graph[i][j] == '#':
        BFS(i,j)
        ans += 1
    
  print(ans)    