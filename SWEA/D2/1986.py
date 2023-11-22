t = int(input())
for t_case in range(1,t+1):
  n = int(input())
  ans = 0
  for i in range(1,n+1):
    if i % 2 == 0:
      ans -= i
    else:
      ans += i
  print('#{} {}'.format(t_case,ans))