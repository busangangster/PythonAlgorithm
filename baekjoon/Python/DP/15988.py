import sys
input = sys.stdin.readline

t = int(input())
dp = [0 for _ in range(1000000)]
dp[0] = 1
dp[1] = 2
dp[2] = 4
dp[3] = 7
for i in range(4,1000000):
  dp[i] = (dp[i-3]+dp[i-2]+dp[i-1]) % 1000000009

for _ in range(t):
  n = int(input())
  print(dp[n-1]%1000000009)