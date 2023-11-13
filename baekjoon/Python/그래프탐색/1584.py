import sys
from collections import deque
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]
def bfs(a,b):
  global ans
  dq = deque()
  dq.append([a,b,0])
  visited[a][b] = 0

  while dq:
    x,y,life = dq.popleft()

    if x == 500 and y == 500:
      ans = min(ans,life)

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < 501) and (0<= yy < 501):
        if not visited[xx][yy] and graph[xx][yy] != 2:
          if graph[xx][yy] == 1:
            dq.append([xx,yy,life+1])
          else:
            dq.appendleft([xx,yy,life])
          visited[xx][yy] = True

n = int(input())
graph = [[0 for _ in range(501)] for _ in range(501)]
visited = [[False for _ in range(501)] for _ in range(501)]
ans = 2147000000

for _ in range(n):
  x1,y1,x2,y2 = map(int,input().split())
  for i in range(min(x1,x2),max(x1,x2)+1):
    for j in range(min(y1,y2),max(y1,y2)+1):
      graph[i][j] = 1

m = int(input())
for _ in range(m):
  x1,y1,x2,y2 = map(int,input().split())
  for i in range(min(x1,x2),max(x1,x2)+1):
    for j in range(min(y1,y2),max(y1,y2)+1):
      graph[i][j] = 2

bfs(0,0)
if ans == 2147000000:
  print(-1)
else:
  print(ans)