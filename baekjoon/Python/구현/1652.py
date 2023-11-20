import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
ans1,ans2 = 0,0
for i in range(n): # 가로
  count = 0
  for j in range(n):
    if graph[i][j] == '.':
      count += 1
    elif graph[i][j] == 'X':
      if count >= 2:
        ans1 += 1
      count = 0
  if count >= 2: # 짐에 안걸리고 벽 끝까지 간 경우
    ans1 += 1
    
for i in range(n): # 세로
  count = 0
  for j in range(n):
    if graph[j][i] == '.':
      count += 1
    elif graph[j][i] == 'X':
      if count >= 2:
        ans2 += 1  
      count = 0
  if count >= 2: # 짐에 안걸리고 벽 끝까지 간 경우
    ans2 += 1

print(ans1,ans2)