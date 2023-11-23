t = int(input())
for t_case in range(1,t+1):
  n = int(input())
  ans = 0
  if n < 3:
    ans = 0
  else:
    ans = n//3

  print('#{} {}'.format(t_case,ans))