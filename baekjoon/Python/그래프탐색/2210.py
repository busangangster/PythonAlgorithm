import sys
input = sys.stdin.readline

graph = [list(input().strip().split()) for _ in range(5)]

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def DFS(a,b,num):
  if len(num) == 6:
    result.add(num)
    return

  for i in range(4):
    x = a + nx[i]
    y = b + ny[i]

    if (0 <= x < 5) and (0 <= y < 5):
      DFS(x,y,num+graph[x][y])

result = set()
for i in range(5):
  for j in range(5):
    DFS(i,j,graph[i][j])

print(len(result))