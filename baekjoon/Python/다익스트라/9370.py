import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  min_dis = [int(1e9) for _ in range(n+1)]
  hq.heappush(q,[0,start])
  min_dis[start] = 0

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > next_dis + cur_dis:
        min_dis[next_node] = next_dis + cur_dis
        hq.heappush(q,[cur_dis+next_dis,next_node])

  return min_dis

t = int(input())
for _ in range(t):
  n,m,t = map(int,input().split())
  s,g,h = map(int,input().split())
  graph = [[] for _ in range(n+1)]
  ans = []
  destination = []
  for _ in range(m):
    a,b,d = map(int,input().split())
    graph[a].append([b,d])
    graph[b].append([a,d])

  s_to = dijkstra(s)
  g_to = dijkstra(g)
  h_to = dijkstra(h)
  
  for _ in range(t):
    x = int(input())
    if (s_to[g] + g_to[h] +h_to[x] == s_to[x]) or (s_to[h] + h_to[g] + g_to[x] == s_to[x]):
      ans.append(x)
  
  print(*sorted(ans))