import sys
input = sys.stdin.readline
from collections import deque

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS(i,j):
  dq = deque()
  dq.append([i,j])
  visited[i][j] = 0
  sword = False 

  while dq:
    x,y = dq.popleft()
    
    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if sword == False:
        if (0 <= xx < n) and (0 <= yy < m) and not visited[xx][yy]:
          if graph[xx][yy] != 1:
            if graph[xx][yy] == 2:
              sword = True
            visited[xx][yy] = visited[x][y] + 1
            dq.append([xx,yy])
      
      else:
        if (0 <= xx < n) and (0 <= yy < m) and not visited[xx][yy]:
          visited[xx][yy] = visited[x][y] + 1
          dq.append([xx,yy])

  return visited[n-1][m-1]

n,m,t = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

# if BFS(0,0) > t or BFS(0,0) == 0:
#   print('Fail')
# else:
#   print(BFS(0,0))
print(BFS(0,0))
for x in visited:
  print(x)
