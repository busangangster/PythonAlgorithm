t = int(input())
for t_case in range(1,t+1):
  n = int(input())
  ans = sorted(list(map(int,input().split())))
  print('#{}'.format(t_case),end=' ')
  print(*ans)