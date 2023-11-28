t = int(input())
for tc in range(1,t+1):
  n,m = map(int,input().split())
  k = n - m
  t = m - k
  print('#{} {} {}'.format(tc,t,k))

  

