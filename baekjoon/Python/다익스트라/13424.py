import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  min_dis = [int(1e9)] *(n+1)
  q = []
  hq.heappush(q,[0,start])
  min_dis[start] = 0

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node, next_dis in graph[cur_node]:
      distance = cur_dis + next_dis
      if min_dis[next_node] > distance:
        min_dis[next_node] = distance
        hq.heappush(q,[distance,next_node])

  return min_dis

t = int(input())
for _ in range(t):
  n,m = map(int,input().split())
  graph = [[] for _ in range(n+1)]
  for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
  
  k = int(input())
  result = 2147000000
  num = 0
  friends = [0] + list(map(int,input().split()))
  ans = [[] for _ in range(n+1)]
  for i in range(1,k+1):
    t = dijkstra(friends[i])
    for j in range(1,n+1):
      ans[j].append(t[j])

  for idx,value in enumerate(ans[1:]):
    plus = sum(value)
    if plus < result:
      result = plus
      num = idx
  print(num+1)
