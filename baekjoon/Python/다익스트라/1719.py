import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  min_dis = [float('inf') for _ in range(n+1)]
  pre_v = ['-'] * (n+1)
  min_dis[start] = 0
  hq.heappush(q,[0,start])

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > next_dis + cur_dis:
        min_dis[next_node] = next_dis + cur_dis
        pre_v[next_node] = cur_node
        hq.heappush(q,[next_dis+cur_dis, next_node])

  return pre_v

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
ans = []
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])

for i in range(1,n+1):
  t = dijkstra(i)
  ans.append(t[1:])

for i in range(n):
  for j in range(n):
    print(ans[j][i],end=' ')
  print()