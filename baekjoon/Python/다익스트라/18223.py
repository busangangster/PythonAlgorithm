import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  min_dis = [int(1e9) for _ in range(v+1)]
  min_dis[start] = 0
  hq.heappush(q,[0,start])

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > cur_dis + next_dis:
        min_dis[next_node] = cur_dis + next_dis
        hq.heappush(q,[cur_dis+next_dis,next_node])
        
  return min_dis

v,e,p = map(int,input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])

first = dijkstra(1)
second = dijkstra(p)
if first[v] == first[p] + second[v]:
  print("SAVE HIM")
else:
  print("GOOD BYE")

