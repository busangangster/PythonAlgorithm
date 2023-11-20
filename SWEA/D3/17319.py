t = int(input())

for t_case in range(1,t+1):
  n = int(input())
  a = input().strip()
  factors = []
  ans = ''
  if n == 1:
    ans = 'No'
  else:
    if a[:n//2] == a[n//2:]:
      ans = 'Yes'
    else:
      ans = 'No'

  print('#{} {}'.format(t_case,ans))
  