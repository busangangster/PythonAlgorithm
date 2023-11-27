t = int(input())
for t_case in range(1,t+1):
  n = int(input())
  a = input()
  b = input()
  cnt = 0
  for i in range(n):
    if a[i] == b[i]:
      cnt += 1

  print('#{} {}'.format(t_case,cnt))