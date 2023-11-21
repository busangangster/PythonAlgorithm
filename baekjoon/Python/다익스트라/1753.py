import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  hq.heappush(q,[0,start])
  min_dis[start] = 0

  while q:
    cur_dis, cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > cur_dis + next_dis:
        min_dis[next_node] = cur_dis + next_dis
        hq.heappush(q,[min_dis[next_node],next_node])

v,e = map(int,input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
min_dis = [int(1e9)] * (v+1)
for _ in range(e):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])

dijkstra(k)
for i in range(1,v+1):
  if min_dis[i] == int(1e9):
    print('INF')
  else:
    print(min_dis[i])