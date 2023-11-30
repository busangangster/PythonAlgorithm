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
    gar,x,y = hq.heappop(q)
      
    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0<= xx <m) and (0<= yy <n) and not visited[xx][yy]:
        if graph[xx][yy] != 'g':
          for i in range(4):
            k = xx + nx[i]
            t = yy + ny[i]
            if (0 <= k < m) and (0 <= t < n):
              if graph[k][i] == 'g':
                hq.heappush(gar+1,xx,yy)
                break
            else:
              hq.heappush(gar,xx,yy)
            visited[xx][yy] = True

n,m = map(int,input().split())
graph = [list(input().strip()) for _ in range(n)]
visited= [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
  for j in range(m):
    if graph[i][j] == 'S':
      BFS(i,j)


