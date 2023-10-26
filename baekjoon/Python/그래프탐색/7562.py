import sys
input = sys.stdin.readline
from collections import deque

nx = [-1,-2,1,2,1,2,-1,-2]
ny = [2,1,2,1,-2,-1,-2,-1]

def BFS(x,y):
  dq = deque()
  dq.append([x,y])
  visited[x][y] = True

  while dq:
    xx,yy = dq.popleft()

    if xx == c and yy == d:
      return graph[c][d]

    for i in range(8):
      xxx = xx + nx[i]
      yyy = yy + ny[i]

      if (0 <= xxx < n) and (0 <= yyy < n) and not visited[xxx][yyy]:
        visited[xxx][yyy] = True
        graph[xxx][yyy] = graph[xx][yy] + 1
        dq.append([xxx,yyy])

t = int(input())
for _ in range(t):
  n = int(input())
  graph = [[0 for _ in range(n)] for _ in range(n)]
  visited = [[False for _ in range(n)] for _ in range(n)]
  a,b = map(int,input().split())
  c,d = map(int,input().split())
  print(BFS(a,b))