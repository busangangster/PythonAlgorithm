import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]


def BFS(x,y):
  xx = [1,0,-1,0]
  yy = [0,1,0,-1]
  dq = deque()
  dq.append([x,y])

  while dq:
    x,y= dq.popleft()
    for i in range(4):
      nx = x + xx[i]
      ny = y + yy[i]

      if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        dq.append([nx,ny])

  return graph[n-1][m-1]

print(BFS(0,0))
