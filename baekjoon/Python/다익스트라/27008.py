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

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > cur_dis + next_dis:
        min_dis[next_node] = cur_dis + next_dis
        hq.heappush(q,[cur_dis+next_dis,next_node])
    
f,p,c,m = map(int,input().split())
graph = [[] for _ in range(f+1)]
min_dis = [float('inf') for _ in range(f+1)]
for _ in range(p):
  a,b,t = map(int,input().split())
  graph[a].append([b,t])
  graph[b].append([a,t])

dijkstra(1)
ans = []
for i in range(1,c+1):
  k = int(input())
  if min_dis[k] <= m:
    ans.append(i)

print(len(ans))
for x in ans:
  print(x)