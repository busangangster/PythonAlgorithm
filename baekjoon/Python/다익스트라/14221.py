import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra():
  q = []
  min_dis = [float('inf') for _ in range(n+1)]
  for store in stores: # 편의점의 위치를 한번에 우선순위 큐에 넣어줌 
    hq.heappush(q,[0,store])
    min_dis[store] = 0

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > next_dis + cur_dis:
        min_dis[next_node] = next_dis + cur_dis
        hq.heappush(q,[next_dis+cur_dis,next_node])

  return min_dis

n,m = map(int,input().split())
graph = [[]for _ in range(n+1)]
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])

p,q = map(int,input().split())
homes = list(map(int,input().split()))
homes.sort() # 거리가 같으면 정정 번호가 낮은 것을 출력하기 위해 오름차순 정렬
stores = list(map(int,input().split()))
ans = float('inf')

t = dijkstra()
for i in homes:
  if ans > t[i]:
    ans = t[i]
    result = i
    
print(result)