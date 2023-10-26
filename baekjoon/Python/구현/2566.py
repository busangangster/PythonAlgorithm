import sys
input = sys.stdin.readline

graph = [list(map(int,input().split())) for _ in range(9)]
ans = -2147000000

for x in graph:
  if ans < max(x):
    ans = max(x)

for i in range(9):
  for j in range(9):
    if graph[i][j] == ans:
      print(ans)
      print(i+1,j+1)
      break