import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  min_dis = [float('inf') for _ in range(n+1)]
  min_dis[start] = 0
  hq.heappush(q,[0,start])

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > next_dis + cur_dis:
        min_dis[next_node] = next_dis + cur_dis
        hq.heappush(q,[next_dis+cur_dis, next_node])

  return min_dis

n,m = map(int,input().split())
graph = [[]for _ in range(n+1)]
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])

x,z = map(int,input().split())
p = int(input())
a = list(map(int,input().split()))
t = dijkstra(x) # 시작지점에서 출발
k = dijkstra(z) # 도착지에서 출발

ans = float('inf')
for i in a:
  ans = min(ans,t[i]+k[i]) # 최단거리를 구해야 하니, 최솟값을 계속 찾아줌

if ans == float('inf'):
  print(-1)
else:
  print(ans)