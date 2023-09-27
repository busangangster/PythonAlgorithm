import sys
from collections import deque
input = sys.stdin.readline

def BFS(n):
  dq = deque()
  dq.append(n)
  
  while dq:
    x = dq.popleft()

    if x == k:
      return visited[x]

    for i in (x-1,x+1,x*2):
      if 0 <= i <= 100000 and not visited[i]:
        visited[i] = visited[x] + 1
        dq.append(i)

n,k = map(int,input().split())
visited = [0 for _ in range(100001)]
print(BFS(n))