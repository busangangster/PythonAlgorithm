import sys
input = sys.stdin.readline

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def DFS(i,j,count):
  global ans
  ans = max(ans,count)

  for k in range(4):
    x = i + nx[k]
    y = j + ny[k]

    if (0 <= x < r) and (0 <= y < c) and graph[x][y] not in visited:
      visited.add(graph[x][y])
      DFS(x,y,count+1)
      visited.remove(graph[x][y])

r,c = map(int,input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = set()
visited.add(graph[0][0])

ans = 1
DFS(0,0,1)
print(ans)