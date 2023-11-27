for t_case in range(1,11):
  n = int(input())
  cnt = 0
  graph = [list(input()) for _ in range(8)]
  for i in range(8): # 가로
    for j in range(8-n+1):
      if graph[i][j:j+n] == graph[i][j:j+n][::-1]:
        cnt += 1
  
  for i in range(8):
    for j in range(8-n+1):
      ans = ''
      for k in range(n):
        ans += graph[k+j][i]
        
      if ans == ans[::-1]:
        cnt += 1

  print('#{} {}'.format(t_case,cnt))