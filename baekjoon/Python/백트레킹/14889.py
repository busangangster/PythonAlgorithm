import sys
input = sys.stdin.readline

def DFS(depth,idx):
  global ans
  if depth == n // 2:
    start,link = 0,0
    for i in range(n):
      for j in range(n):
        if visited[i] and visited[j]:
          start += graph[i][j]

        elif not visited[i] and not visited[j]:
          link += graph[i][j]

    ans = min(ans,abs(start-link))
    return ans
  
  for i in range(idx,n):
    if not visited[i]:
      visited[i] = True
      DFS(depth+1,i+1)
      visited[i] = False

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
ans = int(1e9)
DFS(0,0)
print(ans)
