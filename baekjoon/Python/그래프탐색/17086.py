import sys
from collections import deque
input = sys.stdin.readline

nx = [1,0,-1,0,1,-1,-1,1]
ny = [0,1,0,-1,1,-1,1,-1]

dq = deque()

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      dq.append([i,j])

while dq:
  x,y = dq.popleft()

  for i in range(8):
    xx = x + nx[i]
    yy = y + ny[i]

    if (0 <= xx < n) and (0 <= yy < m):
      if graph[xx][yy] == 0:
        graph[xx][yy] = graph[x][y] + 1
        dq.append([xx,yy])

print(max(map(max,graph))-1)
print(list(map(max,graph)))
#2차원 리스트 내 모든 1차원 원소의 최댓값을 구하기 위해서는 map 함수를 사용하면 효과적입니다.
# map 함수에 max 함수와 이중 리스트를 입력해 주면,
# 1차원 리스트들 중에서 인덱스 고려없이 최댓값을 포함하는 리스트를 반환합니다.
# 이제 반환값을 다시 한번 max 함수에 입력해 주면 최종적으로 원소의 최댓값을 구할 수 있습니다.


nx = [1,0,-1,0,1,-1,-1,1]
ny = [0,1,0,-1,1,-1,1,-1]

def BFS(a,b):
  dq = deque()
  dq.append([a,b,0])
  visited[a][b] = True
  cnt = 0

  while dq:
    x,y,cnt = dq.popleft()

    for i in range(8):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < m) and not visited[xx][yy]:
        if graph[xx][yy] == 1:
          ans.append(cnt + 1)
          return
        else:
          visited[xx][yy] = True
          dq.append([xx,yy,cnt + 1])

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      visited = [[False for _ in range(m)] for _ in range(n)]
      BFS(i,j)
      
print(max(ans))