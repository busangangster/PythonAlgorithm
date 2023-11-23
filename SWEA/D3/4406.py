t = int(input())
for t_case in range(1,t+1):
  a = ['a','e','i','o','u']
  s = input().strip()
  ans = ''
  for x in s:
    if x not in a:
      ans += x

  print('#{} {}'.format(t_case,ans))
    
