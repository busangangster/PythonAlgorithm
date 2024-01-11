import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
  q = []
  min_dis = [float('inf') for _ in range(n+1)]
  min_dis[start] = 0
  hq.heappush(q, (0, start))

  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if prime[arr[cur_node]+arr[next_node]]:
        if min_dis[next_node] > cur_dis + next_dis:
          min_dis[next_node] = cur_dis + next_dis
          hq.heappush(q,(next_dis+cur_dis,next_node))
        
  return min_dis[n]

n,m = map(int,input().split())
arr = [0] + list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
prime = [True]*(10**7+1)
        
for _ in range(m):
  u,v,w = map(int,input().split())
  graph[u].append((v,w))
  graph[v].append((u,w))
  
for i in range(2,len(prime)):
    if prime[i] == True:
        for j in range(i+i,len(prime),i):
            prime[j] = False

k = dijkstra(1)
if k == float('inf'):
  print('Now where are you?')
else:
  print(k)