import sys
import heapq as hq
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS(i,j):
  dq = []
  hq.heapify(dq)
  visited[i][j] = True
  hq.heappush(dq,[0,i,j])

  while dq:
    cnt,x,y = hq.heappop(dq)

    if x == n-1 and y == n-1:
      return cnt

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <=yy < n) and not visited[xx][yy]:
        if graph[xx][yy] == 0:
          hq.heappush(dq,[cnt+1,xx,yy])
        else:
          hq.heappush(dq,[cnt,xx,yy])

        visited[xx][yy] = True

n = int(input())
graph = [list(map(int,input().strip())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
print(BFS(0,0))