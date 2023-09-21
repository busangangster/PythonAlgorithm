import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m): # 정점이 4개, 간선의 개수가 5인 그래프 만들기. 양방향
  a = list(map(int,input().split()))
  graph[a[0]].append(a[1])
  graph[a[1]].append(a[0])

for i in graph: # 작은 곳부터 방문함으로 오름차순 정렬
  i.sort()

def DFS(graph,v,visited):
  visited[v] = True
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      DFS(graph,i,visited)

def BFS(graph,v,visited):
  dq = deque([v])
  
  visited[v] = True
  while dq:
    t = dq.popleft()
    print(t,end=' ')
    for i in graph[t]:
      if not visited[i]:
        dq.append(i)
        visited[i] = True

visited = [False] * (n+1)
DFS(graph,v,visited)
print()
visited = [False] * (n+1)
BFS(graph,v,visited)