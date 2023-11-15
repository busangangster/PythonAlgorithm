import sys
import heapq as hq
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]
def BFS(a,b):
  q = []
  hq.heappush(q,[0,a,b])
  visited[a][b] = True

  while q:
    wall,x,y = hq.heappop(q)

    if x == m-1 and y == n-1:
      return wall

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < m) and (0 <= yy < n) and not visited[xx][yy]:
        if graph[xx][yy] == 1: # 벽을 부숴야 하는 경우
          hq.heappush(q,[wall+1,xx,yy])
        else: # 안부셔도 되는 경우
          hq.heappush(q,[wall,xx,yy])
        visited[xx][yy] = True
  
n,m = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
print(BFS(0,0))