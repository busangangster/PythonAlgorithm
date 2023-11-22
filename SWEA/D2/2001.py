t = int(input())
for t_case in range(1,t+1):
  n,m = map(int,input().split())
  ans = -float('inf')
  graph = [list(map(int,input().split())) for _ in range(n)]
  for i in range(n-m+1):
    for j in range(n-m+1):
      fly = 0
      for k in range(m):
        for l in range(m):
          fly += graph[i+k][j+l]
      
      ans = max(ans,fly)
  
  print('#{} {}'.format(t_case,ans))
        