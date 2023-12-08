t = int(input())
for tc in range(1,t+1):
  n = int(input())
  a = list(map(int,input().split()))
  dp = [1] * n
  for i in range(1,n):
    for j in range(0,i):
      if a[i] > a[j]:
        dp[i] = max(dp[i],dp[j]+1)

  print('#{} {}'.format(tc,max(dp))) 
  