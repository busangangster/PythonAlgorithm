import sys
from collections import deque
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS(a,b):
  dq = deque()
  dq.append([a,b,0])
  visited[a][b] = True

  while dq:
    x,y,life = dq.popleft()

    if x == 500 and y == 500: # 세준이가 (500,500)에 도달 가능하면
      return life # 잃는 생명 출력
      
    for i in range(4): # 상하좌우 탐색
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < 501) and (0 <= yy < 501): # 좌표가 범위 안에 있으면서 
        if not visited[xx][yy] and graph[xx][yy] != 2: # 방문하지 않았고, 죽음의 구역이 아닌 경우
          if graph[xx][yy] == 1: # 위험한 구역이면 생명 1 감소
            dq.append([xx,yy,life+1]) # 0-1 BFS 알고리즘.
          else:
            dq.appendleft([xx,yy,life]) # 0-1 BFS 알고리즘
          visited[xx][yy] = True

  return -1 # 도달하지 못하면 -1 출력

graph = [[0 for _ in range(501)] for _ in range(501)] # 안전구역으로 초기화 된 그래프
visited = [[False for _ in range(501)] for _ in range(501)] # 방문여부 확인 

n = int(input())
for _ in range(n): # 위험한 구역을 그래프에 1로 표시
  x1,y1,x2,y2 = map(int,input().split())
  for i in range(min(x1,x2),max(x1,x2)+1):
    for j in range(min(y1,y2),max(y1,y2)+1):
      graph[i][j] = 1

m = int(input())
for _ in range(m): # 죽음의 구역을 그래프에 2로 표시 
  x1,y1,x2,y2 = map(int,input().split())
  for i in range(min(x1,x2),max(x1,x2)+1):
    for j in range(min(y1,y2),max(y1,y2)+1):
      graph[i][j] = 2

print(BFS(0,0))