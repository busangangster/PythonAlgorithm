import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().strip())) for _ in range(n)]
result = []

def BFS(graph,a,b):
  dq = deque()
  dq.append([a,b])
  graph[a][b] = 0
  cnt = 0
  cnt += 1

  nx = [-1,0,1,0]
  ny = [0,1,0,-1]

  while dq:
    x,y = dq.popleft()
    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and ( 0 <= yy < n) and graph[xx][yy] == 1:
        graph[xx][yy] = 0
        dq.append([xx,yy])
        cnt += 1
  return cnt

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      cnt = BFS(graph,i,j)
      result.append(cnt)

print(len(result))
result.sort()
for x in result:
  print(x)
