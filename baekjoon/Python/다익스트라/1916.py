import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  min_dis[start] = 0
  hq.heappush(q,[0,start])

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue
    for next_node, next_dis in graph[cur_node]:
      distance = cur_dis + next_dis
      if min_dis[next_node] > distance:
        min_dis[next_node] = distance
        hq.heappush(q,[distance,next_node])

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
min_dis = [int(1e9)] * (n+1)
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])

x,y = map(int,input().split())

dijkstra(x)
print(min_dis[y])