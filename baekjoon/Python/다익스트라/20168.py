import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  global result
  q = []
  hq.heappush(q,[0,0,start])

  while q:
    max_cost, total_cost,node = hq.heappop(q)

    if total_cost > c:
      continue
    for x in graph[node]:
      cur_cost = total_cost + x[1]
      if cur_cost > c or visited[node][x[0]]:
        continue
      elif x[0] == b:
        result = min(result,max(max_cost,x[1]))
      visited[node][x[0]] = True
      hq.heappush(q,[max(max_cost,x[1]),cur_cost,x[0]])

n,m,a,b,c = map(int,input().split())
result = int(1e9)
visited = [[False for _ in range(n+1)] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
  j,k,p = map(int,input().split())
  graph[j].append([k,p])
  graph[k].append([j,p])

dijkstra(a)
if result == int(1e9):
  print(-1)
else:
  print(result)
