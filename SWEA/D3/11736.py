t = int(input())
for tc in range(1,t+1):
  n = int(input())
  a = list(map(int,input().split()))
  cnt = 0
  for i in range(n-2):
    if a[i+1] == max(a[i],a[i+1],a[i+2]) or a[i+1] == min(a[i],a[i+1],a[i+2]):
      continue
    else:
      cnt += 1
  print('#{} {}'.format(tc, cnt))