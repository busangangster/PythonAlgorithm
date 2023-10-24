import sys
from collections import deque
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS(a,b):
  global t_s,t_w
  s = 0
  w = 0
  dq = deque()
  dq.append([a,b])
  visited[a][b] = True
  if graph[a][b] == 'v':
    w += 1
  elif graph[a][b] == 'k':
    s += 1

  while dq:
    x,y = dq.popleft()

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < m):
        if not visited[xx][yy] and graph[xx][yy] != '#':
          if graph[xx][yy] == 'v':
            w += 1
          elif graph[xx][yy] == 'k':
            s += 1
          
          visited[xx][yy] = True
          dq.append([xx,yy])

  if s > w:
    t_s += s
  else:
    t_w += w 

n,m = map(int,input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
t_s,t_w = 0,0

for i in range(n):
  for j in range(m):
    if not visited[i][j] and graph[i][j] != '#':
      BFS(i,j)

print(t_s,t_w)