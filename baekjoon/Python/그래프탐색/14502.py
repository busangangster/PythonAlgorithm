import sys
import copy
from collections import deque
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS():
  global ans
  dq = deque()
  cur_graph = copy.deepcopy(graph)

  for i in range(n):
    for j in range(m):
      if cur_graph[i][j] == 2:
        dq.append([i,j])

  while dq:
    x,y = dq.popleft()
    
    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < m):
        if cur_graph[xx][yy] == 0:
          cur_graph[xx][yy] = 2
          dq.append([xx,yy])

  cnt = 0
  for x in cur_graph:
    cnt += x.count(0)
  
  ans = max(ans,cnt)

def wall(cnt):
  if cnt == 3:
    BFS()
    return
    
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        wall(cnt+1)
        graph[i][j] = 0

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = -2147000000
wall(0)
print(ans)