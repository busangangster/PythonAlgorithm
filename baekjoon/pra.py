import sys
input = sys.stdin.readline
from collections import deque

def BFS(v):
  dq = deque()
  dq.append([v,0])
  visited[v] = True

  while dq:
    x,time = dq.popleft()

    if x == d:
      return time

    for k in (2*x,x-1,x+1):
      if 0 <= k < 200001 and not visited[k]:
        visited[k] = True
        if k == 2*x:
          dq.append([k,time])

        elif k == x-1:
          dq.append([k,time+1])
        
        elif k == x+1:
          dq.append([k,time+1])

n,d = map(int,input().split())
visited = [False] * 20
print(BFS(n))
print(visited)
