for t_case in range(1,11):
  n = int(input())
  graph = [list(map(int,input().split())) for _ in range(n)]
  cnt = 0
  for i in range(n):
    flag = 0
    for j in range(n):
      if graph[j][i] == 1:
        flag = 1
      elif graph[j][i] == 2:
        if flag == 1:
          cnt += 1
          flag = 0
  print('#{} {}'.format(t_case,cnt))