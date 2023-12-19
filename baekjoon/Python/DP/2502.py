import sys
input = sys.stdin.readline
d,k = map(int,input().split())

for i in range(1,100000):
  for j in range(1,100000):
    dp = [0 for _ in range(d)]
    dp[0] = i
    dp[1] = j
    for p in range(2,d):
      dp[p] = dp[p-1] + dp[p-2]
    
    if dp[-1] == k:
      print(dp[0])
      print(dp[1])
      exit()
