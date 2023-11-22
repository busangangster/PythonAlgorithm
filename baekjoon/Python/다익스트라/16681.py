import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(v):
  q = []
  hq.heappush(q,[0,v])
  min_dis = [float('inf')] * (N+1)
  min_dis[v] = 0

  while q:
    cur_dis, cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node, next_dis in graph[cur_node]:
      if min_dis[next_node] > next_dis + cur_dis and h[cur_node] < h[next_node]:
        min_dis[next_node] = next_dis + cur_dis
        hq.heappush(q,[min_dis[next_node],next_node])
  
  return min_dis

N,M,D,E = map(int,input().split())
h = [0] + list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
ans = -float('inf')
for _ in range(M):
  a,b,n = map(int,input().split())
  graph[a].append([b,n])
  graph[b].append([a,n])

start = dijkstra(1)
end = dijkstra(N)

for i in range(2,N):
  ans = max(ans,h[i]*E - (start[i]+end[i])*D)

if ans == -float('inf'):
  print("Impossible")
else:
  print(ans)