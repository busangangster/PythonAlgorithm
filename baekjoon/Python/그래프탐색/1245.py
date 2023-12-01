import sys
from collections import deque
input = sys.stdin.readline

nx = [-1,0,1,0,1,1,-1,-1]
ny = [0,1,0,-1,1,-1,-1,1]
def BFS(a,b):
  global ans
  dq = deque()
  dq.append([a,b])
  visited[a][b] = True
  flag = True

  while dq:
    x,y = dq.popleft()

    for i in range(8):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0<= xx <n) and (0<= yy <m):
        if graph[xx][yy] == graph[x][y]:
          if not visited[xx][yy]:
            dq.append([xx,yy])
            visited[xx][yy] = True

        elif graph[xx][yy] > graph[x][y]:
          flag = False

  if flag == True:
    ans += 1

n,m = map(int,input().split())
ans = 0
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
  for j in range(m):
    if not visited[i][j]:
      BFS(i,j)

print(ans)