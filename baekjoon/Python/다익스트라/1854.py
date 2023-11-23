import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  hq.heappush(q,[0,start])
  min_dis[start][0] = 0

  while q:
    cur_dis,cur_node = hq.heappop(q)

    for next_node,next_dis in graph[cur_node]:
      distance = cur_dis + next_dis
      if min_dis[next_node][k] > distance:
        min_dis[next_node][k] = distance
        min_dis[next_node] = sorted(min_dis[next_node])
        hq.heappush(q,[distance,next_node])

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
t = [[] for _ in range(n+1)]
min_dis = [[float('inf')]*(k+1) for _ in range(n+1)]
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])

dijkstra(1)

for x in min_dis:
  x.sort()

for i in range(1,len(min_dis)):
  if len(min_dis[i]) < k:
    print(-1)
  elif min_dis[i][k-1] == float('inf'):
    print(-1)
  else:
    print(min_dis[i][k-1])
