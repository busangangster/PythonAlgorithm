import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def DFS(x,y):
  dx = [1,0,-1,0]
  dy = [0,1,0,-1]

  for i in range(4):
    xx = x + dx[i]
    yy = y + dy[i]

    if (0<= xx < M) and (0 <= yy < N) and arr[xx][yy] == 1:
      arr[xx][yy] = -1  # 확인과정 
      DFS(xx,yy) 

t = int(input())

for _ in range(t):
  cnt= 0
  M,N,K = map(int,input().split())
  arr = [[0]*N for _ in range(M)]

  for _ in range(K):
    x,y = map(int,input().split())
    arr[x][y] = 1
  
  for i in range(M):
    for j in range(N):
      if arr[i][j] == 1:
        DFS(i,j)
        cnt += 1
  print(cnt)


