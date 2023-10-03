import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
  dq = deque()
  dq.append([v,[v]])

  while dq:
    x,ans = dq.popleft()

    if x == 1:
      print(len(ans)-1)
      print(*ans)
      break
    
    else:
      if not visited[x]:
        visited[x] = 1
        if 1<= x <= 1000000 and x % 3 == 0:
          dq.append([x//3,ans+[x//3]])
        if 1<= x <= 1000000 and x % 2 == 0:
          dq.append([x//2,ans + [x//2]])
        dq.append([x-1,ans + [x-1]])

n = int(input())
visited = [0 for _ in range(1000001)]
BFS(n)
