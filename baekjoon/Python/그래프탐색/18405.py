import sys
from collections import deque
input = sys.stdin.readline

# 바이러스가 없는 부분 즉, 0부터 bfs를 돌면 시간초과 발생 ! 
# 바이러스가 존재하는 부분부터 bfs를 돌아야 함 

nx = [-1,0,1,0]
ny = [0,1,0,-1]

n,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
S,X,Y = map(int,input().split())
virus = []

for i in range(n):
  for j in range(n):
    if graph[i][j] != 0:
      virus.append([graph[i][j],0,i,j])

virus.sort()
dq = deque(virus)

while dq:
  v,s,x,y = dq.popleft()

  if s == S:
    break

  for i in range(4):
    xx = x + nx[i]
    yy = y + ny[i]

    if (0 <= xx < n) and (0 <= yy < n) and graph[xx][yy] == 0:
      graph[xx][yy] = v
      dq.append([v,s+1,xx,yy])
      
print(graph[X-1][Y-1])