import sys
from collections import deque
input = sys.stdin.readline

nx = [1,0,-1,0]
ny = [0,1,0,-1]

def BFS(a,b):
  global t_w,t_s
  sheep, wolf = 0,0 # 구역 안에서 양과 늑대의 수 확인

  dq = deque()
  dq.append([a,b])
  visited[a][b] = True

  if graph[a][b] == 'o': # 초기 좌표가 빈 필드가 아닌 늑대 or 양일 경우
    sheep += 1
  elif graph[a][b] == 'v':
    wolf += 1

  while dq:
    x,y = dq.popleft()

    for i in range(4): # 상하좌우 탐색
      xx = x + nx[i]
      yy = y + ny[i]  

      if (0 <= xx < r) and (0 <= yy < c) and graph[xx][yy] != '#' and not visited[xx][yy]:
        # 이동한 칸이 범위에서 벗어나지 않으면서, 펜스가 아니고, 아직 방문하지 않은 경우
        if graph[xx][yy] == 'o':
          sheep += 1
        elif graph[xx][yy] == 'v':
          wolf += 1
        
        visited[xx][yy] = True
        dq.append([xx,yy])

  if sheep > wolf: # 하나의 영역이 끝난 경우 조건에 따라 늑대 or 양 제거 
    t_s += sheep
  else:
    t_w += wolf

r,c = map(int,input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)] 
t_s, t_w = 0,0 # 아침까지 살아있는 늑대 or 양을 확인하기 위한 변수

for i in range(r):
  for j in range(c):
    if graph[i][j] != '#' and not visited[i][j]:
      BFS(i,j)

print(t_s,t_w,end=' ')


