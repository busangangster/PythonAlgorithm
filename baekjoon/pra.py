import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
nx = [-1,0,1,0]
ny = [0,1,0,-1]
dq = deque()
ans = 0

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      dq.append([i,j])

def BFS():
  while dq:
    x,y = dq.popleft()

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < m) and graph[xx][yy] == 0:
        graph[xx][yy] = graph[x][y] + 1
        dq.append([xx,yy])
BFS()
for i in graph:
  if i.count(0) >= 1:
    print(-1)
    sys.exit()
  ans = max(ans,max(i))

print(ans-1)
