import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  min_dis = [float('inf') for _ in range(n+1)]
  min_dis[start] = 0
  hq.heappush(q,[0,start])

  while q:
    cost,node = hq.heappop(q)

    if min_dis[node] < cost:
      continue

    for n_node,basic,extra,time in graph[node]:
      # 비용 계산 !! 
      if time >= 10: 
        charge = basic + (time-10)*extra
      else:
        charge = basic
      # 최소 비용으로 갈 수 있도록 갱신
      if min_dis[n_node] > charge+cost: 
        min_dis[n_node] = charge+cost
        pre_v[n_node] = node # 거점의 수를 알기 위해 pre_v라는 리스트에 거점 입력
        hq.heappush(q,[charge+cost,n_node])

  return min_dis

n,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
pre_v = [n] * (n+1)
for _ in range(r):
  a,b,c,d,e = map(int,input().split())
  graph[b].append([a,c,d,e]) # 최소 비용 경로가 여러가지 존재하면 거점의 수를 최소로 가기 위해 목적지 -> 출발지로 이동

t = dijkstra(n)
path = [1] # 정점을 역추적하면서 몇개의 정점을 방문했는지 확인 
now = 1
while now != n:
  now = pre_v[now]
  path.append(now)

if t[1] == float('inf'):
  print('It is not a great way.')
else:
  print(t[1],len(path))