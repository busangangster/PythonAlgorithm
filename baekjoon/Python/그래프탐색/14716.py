import sys
from collections import deque
input = sys.stdin.readline

nx = [1,0,-1,0,1,1,-1,-1]
ny = [0,1,0,-1,1,-1,1,-1]

def BFS(a,b):
  dq = deque()
  dq.append([a,b])
  visited[a][b] = True
  visited[a][b] = 0
  
  while dq:
    x,y = dq.popleft()

    for i in range(8):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < m):
        if not visited[xx][yy] and graph[xx][yy] == 1:
          visited[xx][yy] = True
          graph[xx][yy] = 0
          dq.append([xx,yy])

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
ans = 0

for i in range(n):
  for j in range(m):
    if not visited[i][j] and graph[i][j] == 1:
      BFS(i,j)
      ans += 1

print(ans)