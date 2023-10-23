import sys
from collections import deque
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS(a,b):
  dq = deque()
  dq.append([a,b])
  visited[a][b] = 0
  check[a][b] = True

  while dq:
    x,y = dq.popleft()

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < m) and not check[xx][yy] and graph[xx][yy] == 1:
        visited[xx][yy] = visited[x][y] + 1
        check[xx][yy] = True
        dq.append([xx,yy])

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
check = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 2 and not check[i][j]:
      BFS(i,j)
    elif graph[i][j] == 0:
      visited[i][j] = 0

for x in visited:
  print(*x)