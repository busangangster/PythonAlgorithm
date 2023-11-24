import sys
import heapq as hq
from collections import deque
input = sys.stdin.readline

def dijkstra():
  q = []
  min_dis = [float('inf') for _ in range(n)]
  hq.heappush(q,[0,s])
  min_dis[s] = 0 

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue
    for next_node,next_dis in graph[cur_node]:
      if visited[cur_node][next_node]:
        continue
      if min_dis[next_node] > cur_dis + next_dis:
        min_dis[next_node] = cur_dis + next_dis
        hq.heappush(q,[min_dis[next_node],next_node])

  return min_dis

def BFS(): # 목적지 -> 출발지 역방향 탐색
  dq = deque()
  dq.append(d)

  while dq:
    cur_node = dq.popleft()

    if cur_node == s: # 출발점에 도착한 경우 
      continue

    for next_node,next_dis in graph_rev[cur_node]:
      if min_dis[next_node] + next_dis == min_dis[cur_node]:
        if not visited[next_node][cur_node]:
          visited[next_node][cur_node] = True
          dq.append(next_node)

while True:
  n,m = map(int,input().split())
  if n == 0 and m == 0:
    break
  s,d = map(int,input().split())
  graph = [[] for _ in range(n)]
  graph_rev = [[] for _ in range(n)]
  visited = [[False for _ in range(n)] for _ in range(n)]
  for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph_rev[b].append([a,c])
  
  min_dis = dijkstra()
  BFS()
  min_dis = dijkstra()
  if min_dis[d] == float('inf'):
    print(-1)
  else:
    print(min_dis[d])

