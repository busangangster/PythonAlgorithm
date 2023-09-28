import sys
from collections import deque
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS(a,b):
  count = 1
  dq = deque()
  dq.append([a,b])
  graph[a][b] = 0

  while dq:
    x,y = dq.popleft()

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]
      if (0 <= xx <n) and (0 <= yy < m) and graph[xx][yy] == 1:
        graph[xx][yy] = 0
        dq.append([xx,yy])
        count += 1

  result.append(count)

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cnt = 0 
result = []

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      BFS(i,j)
      cnt += 1

if result == []:
  print(cnt)
  print(0)
else:
  print(cnt)
  print(max(result))