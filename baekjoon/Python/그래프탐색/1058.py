import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
  global ans
  dq = deque()
  dq.append([v,0])
  visited[v] = True
  cnt = 0

  while dq:
    x,y = dq.popleft()
    
    if y >= 2:
      continue

    for k in graph[x]:
      if not visited[k]:
        visited[k] = True
        dq.append([k,y+1])
        cnt += 1
        
  if cnt > ans:
    ans = cnt

n = int(input())
ans = 0
graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
  a = list(input().strip())
  for j in range(n):
    if a[j] == 'Y':
      graph[i].append(j+1)

for i in range(1,n+1):
  visited = [False] * (n+1)
  BFS(i)

print(ans)

