import sys
import heapq as hq
input = sys.stdin.readline

nx = [1,0,-1,0,0,1,2,3,2,1,0,-1,-2,-3,-2,-1]
ny = [0,1,0,-1,3,2,1,0,-1,-2,-3,-2,-1,0,1,2]
def dijkstra():
  q = []
  hq.heappush(q,[0,0,0])
  min_dis[0][0] = 0
  ans = float('inf')

  while q:
    cur_cost,x,y = hq.heappop(q)

    if min_dis[x][y] < cur_cost:
      continue
    
    to_n = (n-1-x) + (n-1-y) # 목적지까지의 거리가 2이하로 남은 경우
    if to_n <= 2:
      ans = min(ans,cur_cost+to_n*t)
    
    for i in range(16):
      xx = x + nx[i]
      yy = y + ny[i]
      if (0<= xx <n) and (0<= yy <n):
        next_cost = 3*t + graph[xx][yy] # 3번 이동했을 때의 위치에서 풀 먹는시간 + 이동하는 데 걸린시간
        if min_dis[xx][yy] > next_cost + cur_cost:
          min_dis[xx][yy] = next_cost + cur_cost
          hq.heappush(q,[next_cost+cur_cost,xx,yy])

  return ans

n,t = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
min_dis = [[float('inf') for _ in range(n)] for _ in range(n)]

ans = dijkstra()
print(ans)