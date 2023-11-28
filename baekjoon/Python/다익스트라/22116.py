import sys
import heapq as hq
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]
def dijkstra():
  q = []
  hq.heappush(q,[0,0,0])
  min_dis[0][0] = 0

  while q:
    h,x,y = hq.heappop(q)

    
    if min_dis[x][y] < h:
      continue

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < n):
        height = max(h,abs(graph[x][y] - graph[xx][yy]))
        if min_dis[xx][yy] > height:
          min_dis[xx][yy] = height
          hq.heappush(q,[height,xx,yy])

  return min_dis

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
min_dis = [[float('inf') for _ in range(n)] for _ in range(n)]
dijkstra()
print(min_dis[n-1][n-1])