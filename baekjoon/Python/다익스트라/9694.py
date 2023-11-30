import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  min_dis = [float('inf') for _ in range(m)]
  min_dis[start] = 0
  hq.heappush(q,[0,start])

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node, next_dis in graph[cur_node]:
      if min_dis[next_node] > cur_dis + next_dis:
        min_dis[next_node] = cur_dis + next_dis
        pre_node[next_node] = cur_node # 역추적을 위해 이전경로 저장
        hq.heappush(q,[cur_dis + next_dis, next_node])

  return min_dis

t = int(input())
for tc in range(1,t+1):
  n,m = map(int,input().split())
  graph = [[] for _ in range(m)]
  pre_node = [0] * m
  for _ in range(n):
    x,y,z = map(int,input().split())
    graph[x].append([y,z]) # 친구 사이니까 양방향 간선으로 표현
    graph[y].append([x,z])

  t = dijkstra(0)
  if t[m-1] == float('inf'):
    print('Case #{}: {}'.format(tc,-1))
  else: # 경로 역추적 
    path = [m-1] 
    now = m-1
    while now != 0:
      now = pre_node[now]
      path.append(now)
    path.reverse()
    print('Case #{}:'.format(tc),end=' ')
    print(*path)