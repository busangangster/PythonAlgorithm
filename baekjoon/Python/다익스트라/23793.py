import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  hq.heappush(q,[0,start])
  min_dis = [float('inf') for _ in range(n+1)]
  min_dis[start] = 0

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > cur_dis + next_dis:
        min_dis[next_node] = cur_dis + next_dis
        hq.heappush(q,[min_dis[next_node],next_node])

  return min_dis

def dijkstra1(start):
  q = []
  hq.heappush(q,[0,start])
  min_dis = [float('inf') for _ in range(n+1)]
  min_dis[start] = 0

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    if cur_node == y:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > cur_dis + next_dis:
        min_dis[next_node] = cur_dis + next_dis
        hq.heappush(q,[min_dis[next_node],next_node])

  return min_dis

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  u,v,w = map(int,input().split())
  graph[u].append([v,w])

x,y,z = map(int,input().split())

first = dijkstra(x)
second = dijkstra(y)
third = dijkstra1(x)

ans1 = first[y] + second[z]
ans2 = third[z]

if ans1 == float('inf'):
  ans1 = -1
if ans2 == float('inf'):
  ans2 = -1

print(ans1,ans2)

