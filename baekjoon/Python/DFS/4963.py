import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def DFS(x,y):
  dx = [1,0,-1,0,1,1,-1,-1]
  dy = [0,1,0,-1,-1,1,1,-1]

  for i in range(8):
    xx = x + dx[i]
    yy = y + dy[i]

    if (0 <= xx < h) and (0 <= yy <w) and island[xx][yy] == 1:
      island[xx][yy] = -1
      DFS(xx,yy)

while True:
  cnt = 0
  w,h = map(int,input().split())
  if w == 0 and h == 0:
    break
  else:
    island = []
    for _ in range(h):
      island.append(list(map(int,input().split())))

    for i in range(h):
      for j in range(w):
        if island[i][j] == 1:
          DFS(i,j)
          cnt += 1

    print(cnt)

