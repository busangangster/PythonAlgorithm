
import sys
from collections import deque
input = sys.stdin.readline

nx = [1,0,-1,0]
ny = [0,1,0,-1]

def BFS(a,b):
  global total_s,total_w
  white, blue = 0,0
  dq = deque()
  dq.append([a,b])
  visited[a][b] = True

  if graph[a][b] == 'W':
    white += 1
  elif graph[a][b] == 'B':
    blue += 1

  while dq:
    x,y = dq.popleft()

    if graph[x][y] == 'W':
      for i in range(4):
        xx = x + nx[i]
        yy = y + ny[i]

        if (0 <= xx < m) and (0 <= yy < n) and not visited[xx][yy] and graph[xx][yy] == 'W':
          white += 1
          visited[xx][yy] = True
          dq.append([xx,yy])

    elif graph[x][y] == 'B':
      for i in range(4):
        xx = x + nx[i]
        yy = y + ny[i]

        if (0 <= xx < m) and (0 <= yy < n) and not visited[xx][yy] and graph[xx][yy] == 'B':
          blue += 1
          visited[xx][yy] = True
          dq.append([xx,yy])

  total_w += white**2
  total_s += blue**2
  
n,m = map(int,input().split())
graph = [list(input().strip()) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
total_w, total_s = 0,0

for i in range(m):
  for j in range(n):
    if not visited[i][j]:
      BFS(i,j)

print(total_w,total_s)



