t = int(input())
for t_case in range(1,t+1):
  l,u,x = map(int,input().split())
  if x > u:
    ans = -1
  else:
    ans = l-x
    if ans <= 0:
      ans = 0
  print('#{} {}'.format(t_case,ans))