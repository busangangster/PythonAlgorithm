import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

if n == 0 or n == 1:
  print(1)
  sys.exit()
else:
  dp[0] = 1
  dp[1] = 1
  dp[2] = 2
  for i in range(3,n+1):
    for j in range(1,i+1):
      dp[i] += (dp[j-1] * dp[i-j])

print(dp[n])