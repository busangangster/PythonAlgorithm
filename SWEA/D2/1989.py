t = int(input())
for t_case in range(1,t+1):
  s = input().strip()
  ans = 0
  if s == s[::-1]:
    ans = 1
  
  print('#{} {}'.format(t_case,ans))
     
