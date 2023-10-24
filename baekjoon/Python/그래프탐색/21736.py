import sys
from collections import deque
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS(a,b):
  global cnt
  dq = deque()
  dq.append([a,b])
  visited[a][b] = True

  while dq:
    x,y = dq.popleft()

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < m):
        if not visited[xx][yy] and graph[xx][yy] != 'X':
          if graph[xx][yy] == 'P':
            dq.append([xx,yy])
            cnt += 1
          else:           
            dq.append([xx,yy])
          visited[xx][yy] = True
  return cnt

n,m = map(int,input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0

for i in range(n):
  for j in range(m):
    if graph[i][j] == 'I':
      ans = BFS(i,j)

if ans == 0:
  print('TT')
else:
  print(ans)

