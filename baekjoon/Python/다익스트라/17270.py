import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  min_dis = [float('inf') for _ in range(v+1)]
  min_dis[start] = 0
  hq.heappush(q,[0,start])

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > next_dis+cur_dis:
        min_dis[next_node] = next_dis+cur_dis
        hq.heappush(q,[next_dis+cur_dis,next_node])
  
  return min_dis

v,m = map(int,input().split())
graph = [[] for _ in range(v+1)]
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])
j,s = map(int,input().split())
ji = dijkstra(j)
sung = dijkstra(s)
min_v = float('inf')

for i in range(1,v+1):
  if i in [j,s]:
    continue
  min_v = min(min_v,ji[i]+sung[i])

k = []
for i in range(1,v+1):
  if i in [j,s]:
    continue
  if ji[i]+sung[i] != min_v:
    continue
  if ji[i] > sung[i]:
    continue
  hq.heappush(k,[ji[i]+sung[i],ji[i],i])

if not k:
  print(-1)
else:
  print(hq.heappop(k)[2])