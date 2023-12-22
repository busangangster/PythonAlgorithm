import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
  for j in range(m):
    dp[i][j] = max(dp[i][j-1],dp[i-1][j],dp[i][j]) + arr[i][j]

print(dp[n-1][m-1])


