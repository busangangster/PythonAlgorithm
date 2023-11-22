import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  hq.heappush(q,[0,start,0])
  min_dis[start][0] = 0

  while q:
    cur_dis,cur_node,p = hq.heappop(q)

    if min_dis[cur_node][p] < cur_dis:
      continue

    if p+1 <= k:
      for next_node,next_dis in graph[cur_node]:
        if min_dis[next_node][p+1] > cur_dis:
          min_dis[next_node][p+1] = cur_dis
          hq.heappush(q,[min_dis[next_node][p+1],next_node,p+1])

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node][p] > cur_dis + next_dis:
        min_dis[next_node][p] = cur_dis + next_dis
        hq.heappush(q,[min_dis[next_node][p],next_node,p])

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
min_dis = [[float('inf') for _ in range(k+1)] for _ in range(n+1)]
for _ in range(m):
  a,b,t = map(int,input().split())
  graph[a].append([b,t])
  graph[b].append([a,t])
dijkstra(1)
print(min(min_dis[n]))