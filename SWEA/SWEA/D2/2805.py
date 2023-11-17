t = int(input())

for t_case in range(1,t+1):
  n = int(input())
  graph = [list(map(int,input())) for _ in range(n)]
  lt = n // 2
  rt = n // 2
  ans = 0
  flag = True
  for i in range(n):
    ans += sum(graph[i][lt:rt+1])
    if flag == True:
      lt -= 1
      rt += 1
      if lt == 0:
        flag = False
    else:
      lt += 1
      rt -= 1

  print('#{} {}'.format(t_case,ans))
