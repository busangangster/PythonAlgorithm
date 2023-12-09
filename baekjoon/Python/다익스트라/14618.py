import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra1():
  q = []
  min_dis = [float('inf') for _ in range(n+1)]
  for x in A:
    min_dis[x] = 0
    hq.heappush(q,[0,x])
  
  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > cur_dis + next_dis:
        min_dis[next_node] = cur_dis + next_dis
        hq.heappush(q,[cur_dis+next_dis,next_node])
  return min_dis

def dijkstra2():
  q = []
  min_dis = [float('inf') for _ in range(n+1)]
  for x in B:
    min_dis[x] = 0
    hq.heappush(q,[0,x])
  
  while q:
    cur_dis,cur_node = hq.heappop(q)

    if min_dis[cur_node] < cur_dis:
      continue

    for next_node,next_dis in graph[cur_node]:
      if min_dis[next_node] > cur_dis + next_dis:
        min_dis[next_node] = cur_dis + next_dis
        hq.heappush(q,[cur_dis+next_dis,next_node])

  return min_dis

n,m = map(int,input().split())
graph = [[]for _ in range(n+1)]
j = int(input())
k = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
for _ in range(m):
  x,y,z = map(int,input().split())
  graph[x].append([y,z])
  graph[y].append([x,z])

first = dijkstra1()
second = dijkstra2()
a = first[j]
b = second[j]
if a != float('inf') and b != float('inf'):
  if a <= b:
    print('A')
    print(a)
  else:
    print('B')
    print(b)

elif a == float('inf') and b != float('inf'):
  print('B')
  print(b)

elif a != float('inf') and b == float('inf'):
  print('A')
  print(a)

elif a == float('inf') and b == float('inf'):
  print(-1)