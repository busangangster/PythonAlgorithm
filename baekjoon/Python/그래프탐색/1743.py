import sys
input = sys.stdin.readline
from collections import deque

nx = [-1,0,1,0]
ny = [0,1,0,-1]
ans = 0

def BFS(i,j):
  global ans
  cnt = 1
  dq = deque()
  dq.append([i,j])
  visited[i][j] = True

  while dq:
    x,y = dq.popleft()

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < m) and visited[xx][yy] == False and graph[xx][yy] == 1:
        visited[xx][yy] = True
        cnt += 1
        dq.append([xx,yy])

  ans = max(ans,cnt)

n,m,k = map(int,input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
 
for _ in range(k):
  a,b = map(int,input().split())
  graph[a-1][b-1] = 1

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      BFS(i,j)

print(ans)