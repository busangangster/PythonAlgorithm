import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  hq.heappush(q,[0,start])
  min_dis[start] = 0

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if cur_node == t:
      return 

    if min_dis[cur_node] < cur_dis:
      continue
    
    for next_node, next_dis in graph[cur_node]:
      distance = next_dis + cur_dis
      if min_dis[next_node] > distance:
        min_dis[next_node] = distance
        hq.heappush(q,[distance,next_node])
  
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
min_dis = [int(1e9)] * (n+1)
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])

s,t = map(int,input().split())

dijkstra(s)
print(min_dis[t])