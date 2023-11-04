import sys
input = sys.stdin.readline

def dfs(x,y,d,ans,fuel):
  if x == n-1:
    return min(ans,fuel)
  
  for k in direction:
    if d != k:
      if (0 <= x < n) and (0 <= y+k < m):
        ans = dfs(x+1,y+k,k,ans,fuel + graph[x+1][y+k])
  
  return ans

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
direction = [-1,0,1]
ans = 2147000000

for i in range(m):
  ans = min(dfs(0,i,2,ans,graph[0][i]),ans)
print(ans)