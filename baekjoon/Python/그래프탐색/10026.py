import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
cnt1 = 0
cnt2 = 0

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS(a,b):
  visited[a][b] = True
  dq = deque()
  dq.append([a,b])

  while dq:
    x,y = dq.popleft()

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < n):
        if graph[xx][yy] == graph[x][y] and visited[xx][yy] == False:
          visited[xx][yy] = True
          dq.append([xx,yy])

visited= [[False for _ in range(n)] for _ in range(n) ]
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      BFS(i,j)
      cnt1 += 1

print(cnt1,end=' ')

visited= [[False for _ in range(n)] for _ in range(n) ]
for i in range(n):
  for j in range(n):
    if graph[i][j] == 'R':
      graph[i][j] = 'G'

for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      BFS(i,j)
      cnt2 += 1

print(cnt2)