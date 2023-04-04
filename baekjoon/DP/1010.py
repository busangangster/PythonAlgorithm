

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n,m = map(int,input().split())
  dy = [[0 for _ in range(m+1)]for _ in range(n+1)]
  for i in range(1,n+1):
    for j in range(1,m+1):
      if i == 1: # 서쪽이 1일 때
        dy[i][j] = j
        continue

      elif i == j: # 서쪽과 동쪽의 수가 같을 때
        dy[i][j] = 1

      else:
        if j > i: # 동쪽이 서쪽보다 클 때
          dy[i][j] = dy[i][j-1] + dy[i-1][j-1]
          
  print(dy[n][m])
    


