import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  min_dis = [float('inf') for _ in range(t+1)]
  min_dis[start] = 0
  hq.heappush(q,[0,start])

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > cur_dis + next_dis:
        min_dis[next_node] = cur_dis+next_dis
        hq.heappush(q,[next_dis+cur_dis,next_node])
        
  return min_dis

t,c,s,e = map(int,input().split())
graph = [[] for _ in range(t+1)]
for _ in range(c):
  x,y,z = map(int,input().split())
  graph[x].append([y,z])
  graph[y].append([x,z])

k = dijkstra(s)
print(k[e])