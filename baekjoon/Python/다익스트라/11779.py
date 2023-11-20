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

    for next_node, next_dis in graph[cur_node]:
      if min_dis[next_node] > cur_dis + next_dis:
        min_dis[next_node] = cur_dis + next_dis
        pre_node[next_node] = cur_node # 경로 역추적을 위해 현 노드 저장
        hq.heappush(q,[min_dis[next_node],next_node])

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])

s,e = map(int,input().split())
min_dis = [int(1e9)] * (n+1)
pre_node = [s] * (n+1)
dijkstra(s)
print(min_dis[e])

path = [e]
now = e
while now != s:
  now = pre_node[now]
  path.append(now)

print(len(path))
path.reverse()
print(*path)