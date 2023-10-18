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

    for k in (2*x,x-1,x+1): # 수빈이가 이동할 수 있는 경우
      if 0 <= k < 100001 and not visited[k]: 
        # 이동한 위치가 범위 안에 존재하고, 아직 방문하지 않았을 떄
        visited[k] = True
        if k == 2*x: # 순간이동을 하는 경우는 초를 증가시키지 않음 
          dq.append([k,time])

        elif k == x-1: # 걷는 경우는 1초 증가 
          dq.append([k,time+1])
        
        elif k == x+1:
          dq.append([k,time+1])

n,d = map(int,input().split())
visited = [False] * 100001
print(BFS(n))
