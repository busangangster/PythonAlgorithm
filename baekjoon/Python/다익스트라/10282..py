import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  global ans
  q = []
  hq.heappush(q,[0,start])
  min_dis[start] = 0

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      distance = cur_dis + next_dis
      if min_dis[next_node] > distance:
        min_dis[next_node] = distance
        hq.heappush(q,[distance,next_node])

    ans = max(ans,cur_dis) # 감염되는 시간을 계속해서 갱신함 

  return ans

t = int(input())
for _ in range(t):
  n,d,c = map(int,input().split())
  graph = [[] for _ in range(n+1)]
  min_dis = [int(1e9)] * (n+1)
  ans = -int(1e9)
  for _ in range(d): # b -> a로 감염됨 
    a,b,s = map(int,input().split())
    graph[b].append([a,s])
  k = dijkstra(c)
  print(len(min_dis) - min_dis.count(int(1e9)),end=' ') # 감염된 컴퓨터 개수
  print(k)
  
  