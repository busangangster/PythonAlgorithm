t = int(input())
for t_case in range(1,t+1):
  n = int(input())
  a = list(map(int,input().split()))
  min_v = 2147000000
  cnt = 0
  for x in a:
    k = abs(x-0)
    min_v = min(k,min_v)
  for x in a:
    if abs(x-0) == min_v:
      cnt += 1

  print('#{} {} {}'.format(t_case,min_v,cnt))