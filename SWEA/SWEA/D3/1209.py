
for t_case in range(1,11):
  n = int(input())
  graph = [list(map(int,input().split())) for _ in range(100)]
  max_v = -2147000000

  for i in range(100): # 가로
    ans = 0
    for j in range(100):
      ans += graph[i][j]
    
    if ans > max_v:
      max_v = ans
  
  ans = 0
  for i in range(100): # 세로
    ans = 0
    for j in range(100):
      ans += graph[j][i]
    
    if ans > max_v:
      max_v = ans

  ans = 0
  for i in range(100): # 왼 위 -> 오른 아래 대각
    ans += graph[i][i]
  
  if ans > max_v:
    max_v = ans

  ans = 0
  for i in range(100):
    ans += graph[i][99-i]
  if ans > max_v:
    max_v = ans
  
  print('#{} {}'.format(t_case,max_v))


  

