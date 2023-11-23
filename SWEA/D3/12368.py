t = int(input())
for t_case in range(1,t+1):
  a,b = map(int,input().split())
  k = a+b
  ans = 0 
  if k < 24:
    ans = k
  elif k%24 == 0:
    ans = 0
  else:
    ans = k%24
  print('#{} {}'.format(t_case,ans))