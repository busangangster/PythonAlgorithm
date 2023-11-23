t = int(input())
for t_case in range(1,t+1):
  a,b = map(int,input().split())
  ans = 0
  if a >= 10 or b >= 10:
    ans = -1
  else:
    ans = a*b
  print('#{} {}'.format(t_case,ans))