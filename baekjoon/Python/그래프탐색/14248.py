import sys
input = sys.stdin.readline
from collections import deque

def BFS(v):
  dq = deque()
  dq.append(v)
  visited[v] = True
  cnt = 1 

  while dq:
    x = dq.popleft()

    t = x + a[x-1]
    k = x - a[x-1]

    if (0 < t <= n) and not visited[t]:
      visited[t] = True
      cnt += 1
      dq.append(t)
    if (0 < k <= n) and not visited[k]:
      visited[k] = True
      cnt += 1
      dq.append(k)
  return cnt

n = int(input())
a = list(map(int,input().split()))
visited = [False] * (n+1)
s = int(input())
print(BFS(s))
