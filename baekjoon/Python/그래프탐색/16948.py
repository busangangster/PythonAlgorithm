import sys
from collections import deque
input = sys.stdin.readline

nx = [-2,-2,0,0,2,2] # 데스 나이트가 이동하는 방향 
ny = [-1,1,-2,2,-1,1]

def BFS(a,b):
  dq = deque()
  dq.append([a,b])
  visited[a][b] = True

  while dq:
    x,y = dq.popleft()

    for i in range(6):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < n) and not visited[xx][yy]:
        # 이동하려는 방향이 체스판을 벗어나지 않으면서 아직 방문하지 않은 경우
        graph[xx][yy] = graph[x][y] + 1 # 이동횟수 1 증가 ! 
        visited[xx][yy] = True
        dq.append([xx,yy])

  if graph[g][h] == 0: # BFS가 끝났을 때 목적지 좌표값이 0이라면 도달 못한거임 
    return -1
  else:
    return graph[g][h] # 도달했으면, 이동 횟수 출력 !

n = int(input())
e,f,g,h = map(int,input().split())
graph = [[0 for _ in range(n)] for _ in range(n)] # 이동횟수 체크를 위해 0으로 초기화
visited = [[False for _ in range(n)] for _ in range(n)]

print(BFS(e,f))
