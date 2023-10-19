import sys
from collections import deque
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS(i,j):
  union = [] # 연합을 이루는 나라들의 좌표를 기록한 리스트
  dq = deque()
  dq.append([i,j])
  visited[i][j] = True 
  union.append([i,j])

  while dq:
    x,y = dq.popleft()
    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < n):
        if not visited[xx][yy] and l <= abs(graph[x][y] - graph[xx][yy]) <= r:
          dq.append([xx,yy])
          union.append([xx,yy])
          visited[xx][yy] = True

  return union

n,l,r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = 0 

while True:
  visited = [[False for _ in range(n)] for _ in range(n)]
  flag = False
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        country = BFS(i,j)
        if len(country) > 1:
          flag = True
          people = sum(graph[x][y] for x,y in country) // len(country)
          for x,y in country:
            graph[x][y] = people
  
  if flag == False:
    break
  ans += 1
        
print(ans)
