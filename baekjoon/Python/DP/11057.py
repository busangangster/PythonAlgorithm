import sys
input = sys.stdin.readline
n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n+1)]
dp[1] = [1] *10

for i in range(2,n+1):
  for j in range(10):
    dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(sum(dp[n]) % 10007)  