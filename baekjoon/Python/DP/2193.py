import sys
input = sys.stdin.readline

n  = int(input())
dp = [0] * n

if n == 1 or n == 2:
  print(1)
  sys.exit()
else:
  dp[0] = 1
  dp[1] = 1
  for i in range(2,n):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[-1])


