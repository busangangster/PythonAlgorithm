import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  min_dis[start] = 0
  hq.heappush(q,[0,start])

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if cur_node != n-1 and arr[cur_node] == 1:
      continue
    if min_dis[cur_node] < cur_dis:
      continue
    for next_node, next_dis in graph[cur_node]:
      distance = cur_dis + next_dis
      if min_dis[next_node] > distance:
        min_dis[next_node] = distance
        hq.heappush(q,[distance,next_node])
    

n,m = map(int,input().split())
arr = list(map(int,input().split()))
graph = [[] for _ in range(n)]
min_dis = [100000*100001] * n
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])

dijkstra(0)
if min_dis[n-1] == int(100000*100001):
  print(-1)
else:
  print(min_dis[n-1])

