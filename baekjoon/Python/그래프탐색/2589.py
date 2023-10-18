import sys
from collections import deque
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS(i,j):
  dq = deque()
  dq.append([i,j])
  visited[i][j] = 1

  while dq:
    x,y = dq.popleft()

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < m) and not visited[xx][yy] and graph[xx][yy] == 'L':
        visited[xx][yy] = visited[x][y] + 1
        dq.append([xx,yy])

  return visited[x][y] - 1

n,m = map(int,input().split())
graph = [list(input().strip()) for _ in range(n)]
ans = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 'L':
      visited = [[0 for _ in range(m)] for _ in range(n)] 
      ans = max(ans,BFS(i,j))

print(ans)
