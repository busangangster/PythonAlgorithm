import sys
import heapq as hq
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]
def dijkstra():
  q = []
  hq.heappush(q, [graph[0][0],0,0,])

  while q:
    rupee,x,y = hq.heappop(q)

    if x == n-1 and y == n-1:
      print('Problem {}: {}'.format(cnt,rupee))
      break

    for i in range(4):
      xx = x + nx[i]
      yy = y + ny[i]

      if (0 <= xx < n) and (0 <= yy < n):
        cost = graph[xx][yy] + rupee

        if min_c[xx][yy] > cost:
          min_c[xx][yy] = cost
          hq.heappush(q,[cost,xx,yy])

cnt = 1
while True:
  n = int(input())
  if n == 0:
    break
  else:
    graph = [list(map(int,input().split())) for _ in range(n)]
    min_c = [[int(1e9) for _ in range(n)] for _ in range(n)]
    dijkstra()
    cnt += 1