import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a.insert(0,0)

dp = [0] * (n+1)

for i in range(1,n+1):
  for j in range(1,i+1):
    dp[i] = max(dp[i],dp[i-j]+a[j])


print(dp[n])