import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  min_dis = [int(1e9) for _ in range(p+1)]
  min_dis[start] = 0
  hq.heappush(q,[0,start])

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > next_dis + cur_dis:
        min_dis[next_node] = next_dis + cur_dis
        hq.heappush(q,[next_dis+cur_dis,next_node])

  return min_dis

c,p,pb,pa1,pa2 = map(int,input().split())
graph = [[] for _ in range(p+1)]
for _ in range(c):
  a,b,l = map(int,input().split())
  graph[a].append([b,l])
  graph[b].append([a,l])

from_pb = dijkstra(pb)
from_pa1 = dijkstra(pa1)
from_pa2 = dijkstra(pa2)

ans1 = from_pb[pa1] + from_pa1[pa2] # pb -> pa1 -> pa2로 가는 경로
ans2 = from_pb[pa2] + from_pa2[pa1] # pb -> pa2 -> pa1으로 가는 경로
result = min(ans1,ans2)
print(result)
