t = int(input())
for t_case in range(1,t+1):
  n = int(input())
  cnt = 0
  a = list(map(int,input().split()))
  k = sum(a) // n
  for x in a:
    if x <= k:
      cnt += 1
  print('#{} {}'.format(t_case,cnt))