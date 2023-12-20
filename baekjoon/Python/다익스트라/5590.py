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
        hq.heappush(q,[next_dis+cur_dis,next_node])

  return min_dis

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a = list(map(int,input().split()))
  if a[0] == 0:
    k = dijkstra(a[1])
    if k[a[2]] == float('inf'):
      print(-1)
    else:
      print(k[a[2]])
  elif a[0] == 1:
    graph[a[1]].append([a[2],a[3]])
    graph[a[2]].append([a[1],a[3]])
