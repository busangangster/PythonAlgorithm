import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  min_dis = [float('inf') for _ in range(n+1)]
  min_dis[start] = 0
  hq.heappush(q,[0,start])
  
  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > cur_dis + next_dis:
        min_dis[next_node] = cur_dis + next_dis
        hq.heappush(q,[next_dis+cur_dis,next_node])

  return min_dis

n = int(input())
a,b,c = map(int,input().split())
m = int(input())
ans = -float('inf')
land = 0
graph = [[] for _ in range(n+1)]
for _ in range(m):
  d,e,l = map(int,input().split())
  graph[d].append([e,l])
  graph[e].append([d,l])

first = dijkstra(a)
second = dijkstra(b)
third = dijkstra(c)
for i in range(1,n+1):
  result = min(first[i],second[i],third[i])
  if result > ans:
    ans = result
    land = i
print(land)