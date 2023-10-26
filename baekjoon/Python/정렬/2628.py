import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
dp[0] = 4
dp[1] = 9
if n == 0:
  print(dp[0])
elif n == 1:
  print(dp[1])
else:
  for i in range(2,n+1):
    dp[i] = dp[i-1] + (dp[i-1]-dp[i-2])

print(dp[n])