import sys
from collections import deque
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS(a,b):
  dq = deque()
  dq.append([a,b])
  visited[a][b] = True

  while dq:
    x,y = dq.popleft()

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < m):
        if not visited[xx][yy] and graph[xx][yy] == 0:
          visited[xx][yy] = True
          dq.append([xx,yy])

n,m = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(1):
  for j in range(m):
    if not visited[i][j] and graph[i][j] == 0:
      BFS(i,j)
      if True in visited[-1]:
        print('YES')
        sys.exit()

print('NO')