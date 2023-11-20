
import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  min_dis = [int(1e9)] * (n+1)
  q = []
  min_dis[start] = 0
  item = 0
  hq.heappush(q,[0,start])

  while q:
    cur_dis, cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node, next_dis in graph[cur_node]:
      distance = cur_dis + next_dis
      if min_dis[next_node] > distance:
        min_dis[next_node] = distance
        hq.heappush(q,[distance,next_node])
  
  for i in range(1,n+1): # 예은이가 수색할 수 있는 범위 내의 모든 아이템의 개수를 구해줌
    if min_dis[i] <= m:
      item += items[i]
  
  return item

n,m,r = map(int,input().split())
items = [0] + list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
ans = -2147000000
for _ in range(r):
  a,b,l = map(int,input().split())
  graph[a].append([b,l])
  graph[b].append([a,l])

for i in range(1,n+1):
  ans = max(ans,dijkstra(i))
print(ans)

