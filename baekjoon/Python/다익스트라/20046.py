import sys
import heapq as hq
input = sys.stdin.readline

nx = [-1,0,1,0,]
ny = [0,1,0,-1]
def dijkstra():
  q = []
  hq.heappush(q,[graph[0][0],0,0])

  while q:
    cur_cost,x,y = hq.heappop(q)

    if x == n-1 and y == m-1:
      return min_dis[x][y]
    
    if cur_cost == -1: # 시작점이 -1인 경우 고려 !!!! 
      return -1 

    if min_dis[x][y] < cur_cost:
      continue

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < m) and graph[xx][yy] != -1:
        cost = graph[xx][yy] + cur_cost
        if min_dis[xx][yy] > cost:
          min_dis[xx][yy] = cost
          hq.heappush(q,[cost,xx,yy])

  return -1

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
min_dis = [[(int(1e9)) for _ in range(m)] for _ in range(n)]  
print(dijkstra())



