

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

m,n,k = map(int,input().split())
arr = [[0]*n for _ in range(m)]
t = 1 # 영역의 넓이
cnt = [] # 영역의 개수

for _ in range(k): # 직사각형으로 그려진 부분들을 1로 설정 
  a,b,c,d = map(int,input().split())
  for i in range(b,d):
    for j in range(a,c):
      if arr[i][j] == 0:
        arr[i][j] = 1

def DFS(x,y):
  global t 
  arr[x][y] = 1  # DFS가 돌때부터 그 자리는 방문했음을 기록 
  dx = [1,0,-1,0]
  dy = [0,1,0,-1]

  for i in range(4): # 상하좌우 탐색
    nx = x + dx[i]
    ny = y + dy[i]
    # 직사각형으로 그려진 부분이 아닌경우
    if (0<= nx < m) and (0<= ny < n) and arr[nx][ny] == 0:
      arr[nx][ny] = 1 # 체크
      t += 1 # 영역 1 증가
      DFS(nx,ny)

for i in range(m):
  for j in range(n):
    if arr[i][j] == 0:
      DFS(i,j)
      cnt.append(t) # 영역을 cnt에 추가 
      t = 1 # 영역 초기화 

cnt.sort()
print(len(cnt))
print(*cnt)

