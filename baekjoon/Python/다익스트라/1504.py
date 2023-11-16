import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  min_dis = [200000*200000+1] * (n+1)
  q = []
  hq.heappush(q,[0,start])
  min_dis[start] = 0

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue
    for next_node,next_dis in graph[cur_node]:
      distance = cur_dis + next_dis
      if min_dis[next_node] > distance:
        min_dis[next_node] = distance
        hq.heappush(q,[distance,next_node])

  return min_dis

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])
v1,v2 = map(int,input().split())

start = dijkstra(1)
v1_way = dijkstra(v1)
v2_way = dijkstra(v2)

first_way = start[v1] + v1_way[v2] + v2_way[n] # 1 -> v1 -> v2 -> n
second_way = start[v2] +v2_way[v1] + v1_way[n] # 1 -> v2 -> v1 -> n

ans = min(first_way,second_way)
if ans < 200000 *200000 + 1:
  print(ans)
else:
  print(-1)