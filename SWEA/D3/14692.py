t = int(input())
for tc in range(1,t+1):
  n = int(input())
  if n % 2 == 0:
    ans = 'Alice'
  else:
    ans = 'Bob'
  print('#{} {}'.format(tc,ans))
