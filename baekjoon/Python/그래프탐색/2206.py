import sys
input = sys.stdin.readline
from collections import deque

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS(a,b,c):
  dq = deque()
  dq.append([a,b,c])
  visited[a][b][c] = 1

  while dq:
    x,y,z = dq.popleft()

    if x == n-1 and y == m-1:
      return visited[x][y][z]

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < m):
        if graph[xx][yy] == 0 and not visited[xx][yy][z]:
          visited[xx][yy][z] = visited[x][y][z] + 1
          dq.append([xx,yy,z])
        elif graph[xx][yy] == 1 and z == 0:
          visited[xx][yy][1] = visited[x][y][0] + 1
          dq.append([xx,yy,1])

  return -1

n,m = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
visited = [[[0,0] for _ in range(m)] for _ in range(n)]
print(BFS(0,0,0))