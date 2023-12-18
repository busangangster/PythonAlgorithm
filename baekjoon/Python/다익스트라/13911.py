import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra1():
  q = []
  min_dis = [float('inf') for _ in range(V+1)]
  for i in mac: # 힙 안에서 맥도날드 지점을 다 집어 넣어서 최단거리 한번에 계산
    hq.heappush(q,[0,i])
    min_dis[i] = 0
  
  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > next_dis + cur_dis:
        min_dis[next_node] = next_dis + cur_dis
        hq.heappush(q,[next_dis+cur_dis,next_node])
  return min_dis

def dijkstra2():
  q = []
  min_dis = [float('inf') for _ in range(V+1)]
  for i in star: # 힙 안에서 스타벅스 지점을 다 집어 넣어서 최단거리 한번에 계산
    hq.heappush(q,[0,i])
    min_dis[i] = 0
  
  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > next_dis + cur_dis:
        min_dis[next_node] = next_dis + cur_dis
        hq.heappush(q,[next_dis+cur_dis,next_node])
  return min_dis

V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
  u,v,w = map(int,input().split())
  graph[u].append([v,w])
  graph[v].append([u,w])

m,x = map(int,input().split())
mac = list(map(int,input().split()))
s,y = map(int,input().split())
star = list(map(int,input().split()))
k = dijkstra1() # 맥세권인지 확인하는 다익스트라
t = dijkstra2() # 스세권인지 확인하는 다익스트라

ans = float('inf')
for i in range(1,V+1):
  if k[i] == 0 or t[i] == 0:
    continue
  elif k[i] == float('inf') or t[i] == float('inf'):
    continue
  else:
    if k[i] <= x and t[i] <= y:
      result = k[i] + t[i]
      ans = min(ans,result)
    else:
      continue

if ans == float('inf'):
  print(-1)
else:
  print(ans)