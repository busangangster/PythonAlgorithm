t = int(input())
for t_case in range(1,t+1):
  n,k = map(int,input().split())
  graph = [list(map(int,input().split())) for _ in range(n)]
  ans = 0

  for i in range(n): # 가로 확인
    cnt = 0
    for j in range(n):
      if graph[i][j] == 1:
        cnt += 1
      else:
        if cnt == k:
          ans += 1
        cnt = 0
    if cnt == k:
      ans += 1

  for i in range(n): # 세로 확인
    cnt = 0
    for j in range(n):
      if graph[j][i] == 1:
        cnt += 1
      else:
        if cnt == k:
          ans += 1
        cnt = 0
    if cnt == k:
      ans += 1

  print('#{} {}'.format(t_case,ans))
