import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra():
  q = []
  min_dis = [float('inf') for _ in range(n+1)]
  for i in test: # 우선순위 큐에 한번에 다 넣고 실행 
    min_dis[i] = 1
    hq.heappush(q,[0,i])
  
  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > next_dis + cur_dis:
        min_dis[next_node] = next_dis + cur_dis
        hq.heappush(q,[next_dis+cur_dis,next_node])

  return min_dis

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m): # 면접장에서 각각의 도시로 가는 역방향으로 간선을 그어줌
  a,b,c = map(int,input().split())
  graph[b].append([a,c])

test = list(map(int,input().split()))
cities = []
ans = -float('inf')

t = dijkstra()

for i in range(1,n+1):
  if t[i] > ans:
    ans = t[i]
    result = i
print(result)
print(ans)