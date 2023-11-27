import sys
import heapq as hq
input = sys.stdin.readline


def dijkstra(start):
  min_dis = [float("inf") for _ in range(v+1)]
  q =[]
  hq.heappush(q,[0,start])
  min_dis[start] = 0
  
  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for nnode,ndis in graph[cur_node]:
      if min_dis[nnode] > ndis + cur_dis:
        min_dis[nnode] = ndis+cur_dis
        hq.heappush(q,[ndis+cur_dis,nnode])

  return min_dis

n,v,e =map(int,input().split())
A,B = map(int,input().split())
member = list(map(int,input().split()))
result = 0
graph = [[]for _ in range(v+1)]
for _ in range(e):
  a,b,c = map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])

for i in member:
  ans = 0
  k = dijkstra(i)
  first = k[A]
  second = k[B]
  if first == float("inf") and second == float("inf"):
    ans = -2
  elif first == float("inf"):
    ans = -1 +second
  elif second == float("inf"):
    ans = first + -1
  else:
    ans = first + second

  result += ans
print(result)
