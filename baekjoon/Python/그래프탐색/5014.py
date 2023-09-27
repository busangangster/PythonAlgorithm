import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
  dq = deque()
  dq.append(v)
  visited[v] = 1

  while dq:
    x = dq.popleft()
    
    if x == g:
      print(visited[x]-1)
      break
    
    for i in (x+u,x-d):
      if 1 <= i <= f and not visited[i]:
        visited[i] = visited[x] + 1
        dq.append(i)
  else:
    print('use the stairs')
  

f,s,g,u,d = map(int,input().split())
visited = [0 for _ in range(1000001)]
BFS(s)