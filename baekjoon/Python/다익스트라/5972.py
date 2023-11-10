import sys
import heapq as hq
input = sys.stdin.readline


def dijkstra(start):
  q = []
  min_dis[start] = 0
  hq.heappush(q,[0,start]) # 초기 거리, 초기 노드 heap에 추가

  while q:
    cur_dis, cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue
    for next_node,next_dis in graph[cur_node]:
      distance = cur_dis + next_dis
      if min_dis[next_node] > distance:
        min_dis[next_node] = distance
        hq.heappush(q,[distance,next_node])

n,m = map(int,input().split())
graph = [[]for _ in range(n+1)]
INF = int(1e9)
min_dis = [INF] * (n+1)
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])

dijkstra(1)
print(min_dis[n])